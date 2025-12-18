from ingest import load_data
from transform import aggregate_monthly
from indicators import add_indicators
from writer import write_partitioned_files

def run_pipeline():
    df = load_data("data/stocks_daily.csv")
    monthly = aggregate_monthly(df)
    enriched = add_indicators(monthly)
    write_partitioned_files(enriched, "output")

if __name__ == "__main__":
    run_pipeline()
