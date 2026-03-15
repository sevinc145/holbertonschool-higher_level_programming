#!/usr/bin/env python3
import csv
import json


def convert_csv_to_json(filename):
    try:
        data = []

        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)

        with open("data.json", "w") as f:
            json.dump(data, f)

        return True

    except Exception:
        return False
