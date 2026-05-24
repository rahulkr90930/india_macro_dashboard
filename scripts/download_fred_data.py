from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from dotenv import load_dotenv

from src.fred_client import download_series_to_csv, search_series


RAW = ROOT / "data" / "raw"


def main() -> None:
    load_dotenv(ROOT / ".env")

    api_key = os.getenv("FRED_API_KEY")
    if not api_key or api_key == "replace_with_your_fred_api_key":
        print("WARNING: FRED_API_KEY is not set. Script will run in fallback mode using public FRED CSV URLs or offline synthetic data generator.")
        api_key = None
    else:
        print("FRED_API_KEY loaded successfully. Fetching official series observations...")

    RAW.mkdir(parents=True, exist_ok=True)

    # Reliable FRED series IDs.
    # CPI: Consumer Price Index: All Items: Total for India
    # 10Y yield: Interest Rates: Long-Term Government Bond Yields: 10-Year: Main (Including Benchmark) for India
    download_series_to_csv(
        series_id="INDCPIALLMINMEI",
        out_path=str(RAW / "cpi_raw.csv"),
        rename_value_to="cpi_index",
        api_key=api_key,
        observation_start="2015-01-01",
    )
    download_series_to_csv(
        series_id="INDIRLTLT01STM",
        out_path=str(RAW / "gsec_10y_raw.csv"),
        rename_value_to="gsec_10y_yield",
        api_key=api_key,
        observation_start="2015-01-01",
    )

    # Optional search example for policy-rate proxy if you want to inspect FRED coverage.
    # We do not rely on it for the core project because the repo rate cycle is best sourced
    # directly from RBI / official CSV input.
    try:
        cb = search_series("Central Bank Rates: Total for India", api_key=api_key, limit=5)
        cb.to_csv(RAW / "fred_india_central_bank_rate_search.csv", index=False)
    except Exception:
        pass

    print("Downloaded CPI and 10Y yield to data/raw/.")


if __name__ == "__main__":
    main()
