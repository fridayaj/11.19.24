# utils.py

import csv

def round_price(price):
    try:
        return f"{float(price):.2f}"
    except (ValueError, TypeError):
        return "0.00"

def remove_duplicates(rows):
    return [dict(t) for t in {tuple(d.items()) for d in rows}]

def write_csv(filepath, data):
    if data:
        with open(filepath, mode="w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

