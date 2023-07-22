"""
anteil bar chart
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


class anteil_bar_chart:
    _data: pd.DataFrame

    def __init__(self, dataframe: pd.DataFrame) -> None:
        self._data = dataframe

    def get_chart(self) -> go.Figure:
        return px.bar(
            x=self._data["Land"],
            y=self._data["Anteil"],
            labels={
                "x": "Land",
                "y": "CO2-Anteil"
            }
        )
