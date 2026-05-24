"""Check prophet cell and raw CSVs."""
import json
import sys
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')

# Check prophet cell
nb_path = 'notebooks/India_Macro_Policy_Risk_Analytics.ipynb'
with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

cells = nb['cells']
for i in [34, 35]:
    c = cells[i]
    src = ''.join(c.get('source', []))
    print(f"\n{'='*80}")
    print(f"=== CELL {i} [{c['cell_type']}] ===")
    print(f"{'='*80}")
    safe = src.encode('ascii', errors='replace').decode('ascii')
    print(safe)

# Check raw CSVs
print("\n" + "="*80)
print("RAW CSV FILES CHECK")
print("="*80)
import os
raw_dir = 'data/raw'
for fname in os.listdir(raw_dir):
    if fname.endswith('.csv'):
        path = os.path.join(raw_dir, fname)
        try:
            df = pd.read_csv(path)
            print(f"\n{fname}: {df.shape}")
            print(f"  Columns: {list(df.columns)}")
            print(f"  Head:\n{df.head(2).to_string()}")
            print(f"  Tail:\n{df.tail(2).to_string()}")
            print(f"  Nulls: {df.isnull().sum().to_dict()}")
        except Exception as e:
            print(f"\n{fname}: ERROR - {e}")
