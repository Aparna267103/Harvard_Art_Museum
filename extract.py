import requests       
from config import API_KEY

CLASSIFICATION_URL = "https://api.harvardartmuseums.org/classification"
OBJECT_URL = "https://api.harvardartmuseums.org/object"

def collect_artifacts(min_objects=2500):
    records = []
    page = 1

    while True:
        params = {
            "apikey": API_KEY,
            "size": 100,
            "page": page
        }

        response = requests.get(CLASSIFICATION_URL, params=params)
        data = response.json()

        if "records" not in data or not data["records"]:
            break

        for cls in data["records"]:
            if cls.get("objectcount", 0) >= 2500:
                records.append(cls["name"])

        if not data.get("info", {}).get("next"):
            break

        page += 1
    return records
