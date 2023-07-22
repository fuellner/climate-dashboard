"""
layout.py
"""
from dash import html, dcc
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from src.constants import MONTHS
from dash import dash_table


def get_layout(anteil_bar_fig: go.Figure, pie_chart: go.Figure, co2_world_data: pd.DataFrame) -> html.Div:
    return html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(
                        html.H1(children="Klima-Dashboard mit plotly dash"),
                        style={"border-bottom": "1px dashed black"}
                    )
                ],
                style={"padding": "10px"}
            ),
            dbc.Row(
                [
                    dbc.Col(
                        html.H2(children="CO2 Länder-Ranking"),
                    )
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(
                        html.P(
                            "Hier sieht man ein Ranking der TOP 10 Länder Weltweit hinsichtlich absolutem und anteiligen CO2-Ausstoss weltweit."
                        )
                    )
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dcc.Graph(figure=anteil_bar_fig)
                    ),
                    dbc.Col(
                        dcc.Graph(figure=pie_chart)
                    )
                ],
                style={"border-bottom": "1px dashed black", "padding": "20px"}
            ),
            dbc.Row(
                [
                    dbc.Col(
                        html.H2(
                            children="Durchschnittliche Temperatur je Monat und Jahr"),
                    )
                ],
                style={"padding-top": "20px"}
            ),
            dbc.Row(
                [
                    dbc.Col([dcc.Dropdown(id="month-dropdown",
                                          options=MONTHS, value="JAN"),
                             dcc.Graph(id="temp-plot-fig")]
                            )
                ],
                style={"padding-top": "20px",
                       "border-bottom": "1px dashed black"}
            ),
            dbc.Row(
                [
                    dbc.Col(
                        html.H2(
                            children="Tabelle: CO2 Emissionen aller Länder weltweit"),
                    )
                ],
                style={"padding-top": "20px"}
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dash_table.DataTable(
                            id='table',
                            columns=[{"name": i, "id": i}
                                     for i in co2_world_data.columns],
                            data=co2_world_data.to_dict('records'),
                            page_size=10
                        )
                    )
                ],
                style={"padding-top": "20px"}
            ),
            dbc.Row(
                dbc.Col(
                    [html.H3("Quellen:"),
                     html.Ul(
                        children=[
                            html.Li(
                                children=[
                                    html.A("EDGAR - Emissions Database for Global Atmospheric Research",
                                           href="https://edgar.jrc.ec.europa.eu/")
                                ]
                            ),
                            html.Li(
                                children=[
                                    html.A("GISS Surface Temperatur",
                                           href="https://data.giss.nasa.gov/gistemp/")
                                ]
                            )
                        ]
                    )]
                )
            )
        ],
        style={
            "padding-top": '50px',
            "padding-left": '150px',
            "padding-right": '150px',
            "padding-bottom": '50px'
        }
    )
