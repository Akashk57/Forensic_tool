import os
import requests

def analyze_all_files(base_path, api='http://127.0.0.1:5000/analyze'):
    for root, _, files in os.walk(base_path):
        for f in files:
            path = os.path.join(root, f)
            try:
                with open(path, 'rb') as file:
                    response = requests.post(api, files={'file': file})
                    print(f"[AI] {path}: {response.json()}")
            except Exception:
                continue

