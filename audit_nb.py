"""Audit notebook: list all cells with type and first line."""
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

nb_path = 'notebooks/India_Macro_Policy_Risk_Analytics.ipynb'
with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

cells = nb['cells']
print(f"Total cells: {len(cells)}")
print("=" * 80)

for i, c in enumerate(cells):
    ct = c['cell_type']
    src_lines = c.get('source', [])
    n_lines = len(src_lines)
    first = ''.join(src_lines[:3]).replace('\n', '\\n')[:200] if src_lines else 'EMPTY'
    print(f"\nCell {i} [{ct}] ({n_lines} lines):")
    print(f"  {first}")
