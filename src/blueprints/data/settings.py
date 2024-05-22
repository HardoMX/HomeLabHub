import yaml

class Site():
    def __init__(self, name, url, description, img, category):
        self.name = name
        self.url = url
        self.description = description
        self.img = img
        self.category = category

CATEGORIES = []
LOCATION = ""
BACKGROUND = ""
SITES = []

with open("blueprints/data/settings.yaml", "r") as file:
    settings = yaml.safe_load(file)
    print(settings)
    CATEGORIES = settings["categories"]
    LOCATION = settings["location"]
    BACKGROUND = f"/static/images/backgrounds/{settings["background"]}"
    
    for site in settings["sites"]:
        icon = f"https://github.com/walkxcode/dashboard-icons/blob/main/png/{site["icon"].lower()}.png?raw=true"
        site = Site(site["name"], site["url"], site["description"], icon, site["category"])
        SITES.append(site)
