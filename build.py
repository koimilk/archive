#!/usr/bin/env python3
"""Scans ./files and writes files.json. Run it whenever you add or remove files."""
import os, json

ROOT = "files"
items = []
for d, _, names in os.walk(ROOT):
    for n in names:
        if n.startswith("."):
            continue
        full = os.path.join(d, n)
        st = os.stat(full)
        items.append({
            "p": os.path.relpath(full, ROOT).replace(os.sep, "/"),
            "s": st.st_size,
            "m": int(st.st_mtime),
        })
items.sort(key=lambda x: x["p"].lower())
with open("files.json", "w", encoding="utf-8") as f:
    json.dump(items, f, separators=(",", ":"))
print(f"Indexed {len(items)} files -> files.json")
