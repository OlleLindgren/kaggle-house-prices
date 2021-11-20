from pathlib import Path
import json
from typing import List

PKG_ROOT = Path(__file__).parent
DATA_ROOT = PKG_ROOT / "data"
RESULTS_DIR = PKG_ROOT / "results"
DATA_ROOT.mkdir(exist_ok=True, parents=False)
RESULTS_DIR.mkdir(exist_ok=True, parents=False)

RESPONSE: str = "SalePrice"
FLOAT_COLS: List[str]
CATEGORICAL_COLS: List[str]

with open(PKG_ROOT / "categorical_cols.json", "r") as f:
    CATEGORICAL_COLS = json.load(f)

if (train_data_tile := DATA_ROOT / "train.csv").exists():
    import pandas as pd
    __df__ = pd.read_csv(train_data_tile, nrows=1, header=0)
    FLOAT_COLS = list(set(__df__.columns) - {RESPONSE} - set(CATEGORICAL_COLS))
    del __df__
