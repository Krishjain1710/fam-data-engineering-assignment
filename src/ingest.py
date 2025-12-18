import pandas as pd

REQUIRED_COLUMNS = {
    "date",
    "volume",
    "open",
    "high",
    "low",
    "close",
    "adjclose",
    "ticker"
}

EXPECTED_TICKERS = {
    "AAPL", "AMD", "AMZN", "AVGO", "CSCO",
    "MSFT", "NFLX", "PEP", "TMUS", "TSLA"
}

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    if not REQUIRED_COLUMNS.issubset(df.columns):
        missing = REQUIRED_COLUMNS - set(df.columns)
        raise ValueError(f"Missing columns: {missing}")

    df["date"] = pd.to_datetime(df["date"], errors="raise")

    numeric_cols = ["volume", "open", "high", "low", "close", "adjclose"]
    df[numeric_cols] = df[numeric_cols].astype(float)

    tickers = set(df["ticker"].unique())
    if tickers != EXPECTED_TICKERS:
        raise ValueError(f"Unexpected tickers found: {tickers}")

    df = df.sort_values(["ticker", "date"]).reset_index(drop=True)

    return df
