# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pandas",
# ]
# ///

import pandas as pd
from pathlib import Path

HERE = Path(__file__).parent.resolve()
PATH = HERE / "annotation_properties.tsv"

if __name__ == "__main__":
    pd.read_csv(PATH, sep="\t").to_csv(PATH, sep="\t", index=False)
