"""
DataSource classes and related functions
"""
import pandas as pd
from dataclasses import dataclass


@dataclass()
class DataSource:
    _data: pd.DataFrame


@dataclass()
class Co2DataSource(DataSource):
    @property
    def all(self) -> pd.DataFrame:
        sorted_data: pd.DataFrame = self._data.sort_values(
            by="CO2_Emissionen", ascending=False)
        sorted_data.set_index("Rang", inplace=True)
        return sorted_data

    @property
    def top10(self) -> pd.DataFrame:
        # def get_top10(self) -> list[str]:
        sorted_data: pd.DataFrame = self._data.sort_values(
            by="CO2_Emissionen", ascending=False)
        sorted_data.set_index("Rang", inplace=True)
        return sorted_data[0:10]
