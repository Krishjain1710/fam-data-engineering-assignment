import pandas as pd

def aggregate_monthly(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["year_month"] = df["date"].dt.to_period("M")

    grouped = df.groupby(["ticker", "year_month"])

    monthly = grouped.agg(
        open=("open", "first"),
        high=("high", "max"),
        low=("low", "min"),
        close=("close", "last")
    )

    monthly = monthly.reset_index()
    monthly["date"] = monthly["year_month"].dt.to_timestamp("M")
    monthly = monthly.drop(columns=["year_month"])

    monthly = monthly.sort_values(["ticker", "date"]).reset_index(drop=True)

    return monthly
