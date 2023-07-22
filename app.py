"""
app.py - entry point of dashboard app
"""

from dash import Dash
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from src.constants import CO2NACHLAENDER, TEMPDATEN, EDGARCO2DATEN
from src.layout.layout import get_layout
from src.layout.components.co2_top10_pie_chart import co2_top10_data_pie_chart
from src.layout.components.anteil_bar_chart import anteil_bar_chart

# data sources
co2_top10_data: pd.DataFrame = pd.read_csv(CO2NACHLAENDER, sep=";")
co2_world_data: pd.DataFrame = pd.read_csv(
    EDGARCO2DATEN, sep=";", encoding="utf-8")
temp_data: pd.DataFrame = pd.read_csv(TEMPDATEN, sep=",")

# create Dash app
app: Dash = Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])

# get the layout
app.layout = get_layout(
    anteil_bar_chart(co2_top10_data).get_chart(),
    co2_top10_data_pie_chart(co2_top10_data).get_chart(),
    co2_world_data
)

# callback function for interactivity


@app.callback(
    Output(component_id="temp-plot-fig", component_property="figure"),
    Input(component_id="month-dropdown", component_property="value")
)
def update_graph(selected_month: str):
    line_fig = px.scatter(temp_data, x="YEAR", y=selected_month, labels={
        "x": "Jahre", "y": "Temperatur"}, trendline="ols")
    return line_fig


if __name__ == "__main__":
    # debug should be set to false for production code
    app.run_server(debug=True)
