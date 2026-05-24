# Run order

1. Create a `.env` file from `.env.example` and add your FRED API key locally.
2. Install dependencies: `pip install -r requirements.txt`
3. Run `python scripts/download_fred_data.py`
4. Put the remaining raw CSVs into `data/raw/`
5. Open `notebooks/India_Macro_Policy_Risk_Analytics.ipynb`
6. Run all cells from top to bottom

### Required raw CSVs

- `iip_raw.csv`
- `unemployment_raw.csv`
- `repo_rate_raw.csv`
- `liquidity_raw.csv`

### Important note

Do not commit your API key. Rotate it because it was exposed in chat.
