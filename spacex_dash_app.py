from pathlib import Path

import dash
import pandas as pd
import plotly.express as px
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

DATA_FILE = Path("spacex_launch_dash.csv")
DATA_URL = (
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
    "IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv"
)


def load_data():
    if DATA_FILE.exists():
        return pd.read_csv(DATA_FILE)

    df = pd.read_csv(DATA_URL)
    df.to_csv(DATA_FILE, index=False)
    return df


spacex_df = load_data()
max_payload = int(spacex_df["Payload Mass (kg)"].max())
min_payload = int(spacex_df["Payload Mass (kg)"].min())

app = dash.Dash(__name__)
site_options = [{"label": "All Sites", "value": "ALL"}] + [
    {"label": site, "value": site} for site in sorted(spacex_df["Launch Site"].unique())
]

app.layout = html.Div(
    children=[
        html.H1(
            "SpaceX Launch Records Dashboard",
            style={
                "textAlign": "center",
                "color": "#1f2937",
                "font-size": 38,
                "marginBottom": "16px",
            },
        ),
        dcc.Dropdown(
            id="site-dropdown",
            options=site_options,
            value="ALL",
            placeholder="Select a launch site",
            searchable=True,
        ),
        html.Br(),
        html.Div(dcc.Graph(id="success-pie-chart")),
        html.Br(),
        html.P("Payload range (kg):", style={"fontWeight": "600"}),
        dcc.RangeSlider(
            id="payload-slider",
            min=min_payload,
            max=max_payload,
            step=500,
            marks={
                value: str(value)
                for value in range(
                    int(min_payload / 1000) * 1000,
                    int(max_payload / 1000 + 1) * 1000 + 1,
                    2000,
                )
            },
            value=[min_payload, max_payload],
        ),
        html.Div(dcc.Graph(id="success-payload-scatter-chart")),
    ],
    style={"maxWidth": "1100px", "margin": "24px auto", "padding": "0 16px"},
)


@app.callback(
    Output(component_id="success-pie-chart", component_property="figure"),
    Input(component_id="site-dropdown", component_property="value"),
)
def get_pie_chart(entered_site):
    if entered_site == "ALL":
        success_by_site = (
            spacex_df.groupby("Launch Site", as_index=False)["class"].sum().rename(
                columns={"class": "Successful Launches"}
            )
        )
        fig = px.pie(
            success_by_site,
            values="Successful Launches",
            names="Launch Site",
            title="Total Successful Launches by Site",
            template="plotly_white",
        )
    else:
        filtered_df = spacex_df[spacex_df["Launch Site"] == entered_site]
        outcome_counts = (
            filtered_df["class"]
            .value_counts()
            .rename_axis("Outcome")
            .reset_index(name="Count")
        )
        outcome_counts["Outcome"] = outcome_counts["Outcome"].map(
            {0: "Failure", 1: "Success"}
        )
        fig = px.pie(
            outcome_counts,
            values="Count",
            names="Outcome",
            title=f"Launch Outcomes for {entered_site}",
            template="plotly_white",
        )

    return fig


@app.callback(
    Output(component_id="success-payload-scatter-chart", component_property="figure"),
    [
        Input(component_id="site-dropdown", component_property="value"),
        Input(component_id="payload-slider", component_property="value"),
    ],
)
def update_scatter_chart(entered_site, payload_range):
    low, high = payload_range
    filtered_df = spacex_df[
        (spacex_df["Payload Mass (kg)"] >= low)
        & (spacex_df["Payload Mass (kg)"] <= high)
    ]

    if entered_site != "ALL":
        filtered_df = filtered_df[filtered_df["Launch Site"] == entered_site]
        title = f"Payload vs. Launch Outcome for {entered_site}"
    else:
        title = "Payload vs. Launch Outcome for All Sites"

    fig = px.scatter(
        filtered_df,
        x="Payload Mass (kg)",
        y="class",
        color="Booster Version Category",
        title=title,
        template="plotly_white",
    )
    fig.update_yaxes(tickvals=[0, 1], ticktext=["Failure", "Success"])
    return fig


if __name__ == "__main__":
    app.run(port=8060)
