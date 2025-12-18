from pathlib import Path
import pandas as pd

def write_partitioned_files(df: pd.DataFrame, output_dir: str) -> None:
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    for ticker, part in df.groupby("ticker"):
        part = part.sort_values("date")
        path = Path(output_dir) / f"result_{ticker}.csv"
        part.to_csv(path, index=False)
