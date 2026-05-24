"""
Run the entire notebook logic as a script to find all errors.
This mirrors what happens when you do "Run All" in Jupyter.
"""
import json
import sys
import traceback

sys.stdout.reconfigure(encoding='utf-8')

nb_path = 'notebooks/India_Macro_Policy_Risk_Analytics.ipynb'
with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

cells = nb['cells']
code_cells = [(i, ''.join(c.get('source', []))) for i, c in enumerate(cells) if c['cell_type'] == 'code' and ''.join(c.get('source', [])).strip()]

# We'll exec each cell in order in a shared namespace
namespace = {}

for cell_idx, src in code_cells:
    print(f"\n--- Running Cell {cell_idx} ---")
    try:
        exec(compile(src, f'<cell_{cell_idx}>', 'exec'), namespace)
        print(f"  [OK] Cell {cell_idx} succeeded")
    except Exception as e:
        print(f"  [ERROR] Cell {cell_idx} failed:")
        traceback.print_exc()
        # Continue to find more errors
        continue

print("\n" + "="*80)
print("DONE - All cells attempted")
