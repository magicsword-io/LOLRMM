import os
import json


def count_yaml_files():
    yaml_dir = "yaml"
    count = len(
        [f for f in os.listdir(yaml_dir) if f.endswith(".yaml") or f.endswith(".yml")]
    )
    return count


def update_badge_json(count):
    badge_data = {
        "schemaVersion": 1,
        "label": "RMM Tools",
        "message": str(count),
        "color": "blue",
    }
    with open("rmm-tools-count.json", "w") as f:
        json.dump(badge_data, f)


if __name__ == "__main__":
    count = count_yaml_files()
    update_badge_json(count)
    print(f"Updated badge count to {count}")
