import pandas as pd

def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["sma_10"] = df.groupby("ticker")["close"].transform(
        lambda x: x.rolling(window=10).mean()
    )

    df["sma_20"] = df.groupby("ticker")["close"].transform(
        lambda x: x.rolling(window=20).mean()
    )

    df["ema_10"] = df.groupby("ticker")["close"].transform(
        lambda x: x.ewm(span=10, adjust=False).mean()
    )

    df["ema_20"] = df.groupby("ticker")["close"].transform(
        lambda x: x.ewm(span=20, adjust=False).mean()
    )

    return df
