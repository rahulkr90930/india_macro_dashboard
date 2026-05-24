import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

nb_path = r'c:\Users\rahul\Desktop\antigrivity\project 1\india_macro_internship_project\notebooks\India_Macro_Policy_Risk_Analytics.ipynb'

with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

cells = nb['cells']
# Print cells 2-18 specifically
for i in range(2, 19):
    c = cells[i]
    if c['cell_type'] == 'code':
        src = ''.join(c.get('source', []))
        print(f'\n=== Cell {i} [code] FULL ===')
        safe = src.encode('ascii', errors='replace').decode('ascii')
        print(safe)
    elif c['cell_type'] == 'markdown':
        src = ''.join(c.get('source', []))
        print(f'\n=== Cell {i} [markdown] ===')
        safe = src.encode('ascii', errors='replace').decode('ascii')
        print(safe)
