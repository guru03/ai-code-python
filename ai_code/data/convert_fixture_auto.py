import json
import os
import django
from django.apps import apps as django_apps

# Setup Django so we can query models dynamically
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ai_code.settings")
django.setup()

# Define which raw JSON files to convert
raw_files = {
    "apps/angular/fixtures/angular_data.json": "angular",
    "apps/javascript/fixtures/javascript_raw.json": "javascript",
    "apps/locations/fixtures/locations_data.json": "locations",
}

# Field renames per app
field_maps = {
    "javascript": {"angular_questions": "javascript_questions"},
    "angular": {},
    "locations": {},
}


def convert(input_path, app_name):
    output_path = input_path.replace("_raw.json", "_fixture.json").replace(
        "data.json", "_fixture.json"
    )

    with open(input_path, "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    # Get the first model in the app (or adjust if multiple models exist)
    app_config = django_apps.get_app_config(app_name)
    model_name = list(app_config.models.keys())[0]  # first model
    model_label = f"{app_name}.{model_name}"

    fixture = []
    for obj in raw_data:
        fields = {}
        for k, v in obj.items():
            if k in ["id", "created_at", "updated_at"]:
                continue  # skip id (pk handled separately) and timestamps
            new_key = field_maps.get(app_name, {}).get(k, k)
            fields[new_key] = v

        fixture.append({"model": model_label, "pk": obj.get("id"), "fields": fields})

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(fixture, f, indent=2)

    print(f"Converted {input_path} → {output_path} with model {model_label}")


if __name__ == "__main__":
    for path, app in raw_files.items():
        if os.path.exists(path):
            convert(path, app)
        else:
            print(f"Skipping {app}, no input file found at {path}")
