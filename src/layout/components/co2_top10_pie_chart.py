"""
co2_top10_data pie_chart
"""
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


class co2_top10_data_pie_chart:
    _data: pd.DataFrame

    def __init__(self, dataframe: pd.DataFrame) -> None:
        self._data = dataframe

    def get_chart(self) -> go.Figure:
        return px.pie(self._data, values="Anteil", names="Land")
