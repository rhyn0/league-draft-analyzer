from collections import namedtuple
from typing import NamedTuple
import pandas as pd

ChampStyles = namedtuple(
    "ChampStyles", ["Attack", "Split", "Siege", "Protect", "Catch"]
)


def _input_styles(name: str) -> ChampStyles:
    return ChampStyles(
        *[
            1 if not (ans := input(f"{field} trait for '{name}' - Y/n ")) else 0
            for field in ChampStyles._fields
        ]
    )


def load_champs(path="../data/Champ-Style.csv") -> pd.DataFrame:
    """Read champ data from existing csv."""
    return pd.read_csv(path, header=0)


def add_champs(df: pd.DataFrame) -> pd.DataFrame:
    """Add a champion to dataframe."""
    df = df.copy()
    name = None
    while name is None:
        name = input("Add which champion? ")
    vals = _input_styles(name)
    df.loc[len(df.index)] = [name] + list(vals)
    return df


def save_champs(df: pd.DataFrame, path="../data/Champ-Style.csv"):
    """Output champ data frame to CSV."""
    df.to_csv(path, header=True)
