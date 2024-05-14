import yaml

CATEGORIES = []

with open("blueprints/data/settings.yaml", "r") as file:
    settings = yaml.safe_load(file)
    print(settings)
    CATEGORIES = settings["categories"]
