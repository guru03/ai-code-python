import json
import os

# Map app names to their raw JSON files, output fixture files, and model names
apps = {
    "angular": {
        "input": "apps/angular/fixtures/angular_data.json",
        "output": "apps/angular/fixtures/angular_fixture.json",
        "model": "angular.angular",
        "field_map": {}  # no renames needed
    },
    "javascript": {
        "input": "apps/javascript/fixtures/javascript_raw.json",
        "output": "apps/javascript/fixtures/javascript_initial_data.json",
        "model": "javascript.javascript",
        "field_map": {
            "angular_questions": "javascript_questions"  # ✅ rename
        }
    },
    "locations": {
        "input": "apps/locations/fixtures/locations_data.json",
        "output": "apps/locations/fixtures/locations_fixture.json",
        "model": "locations.location",
        "field_map": {}  # add renames here if needed
    }
}

def convert(app_config):
    with open(app_config["input"], "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    fixture = []
    for obj in raw_data:
        fields = {}
        for k, v in obj.items():
            if k == "id":
                continue  # handled separately as pk
            # Rename fields if mapping exists
            new_key = app_config["field_map"].get(k, k)
            fields[new_key] = v

        fixture.append({
            "model": app_config["model"],
            "pk": obj.get("id"),
            "fields": fields
        })

    with open(app_config["output"], "w", encoding="utf-8") as f:
        json.dump(fixture, f, indent=2)

if __name__ == "__main__":
    for app_name, config in apps.items():
        if os.path.exists(config["input"]):
            convert(config)
            print(f"Converted fixture for {app_name} → {config['output']}")
        else:
            print(f"Skipping {app_name}, no input file found.")
