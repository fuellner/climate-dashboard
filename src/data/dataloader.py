"""
dataloader.py
"""
from pd import DataFrame


def loadData(path: str) -> pd.DataFrame:
    return pd.read_csv(path, sep=";", encoding="utf-8")  # type: ignore
