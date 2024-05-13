import yaml

class Site:
    def __init__(self, name, url, img, category):
        self.name = name
        self.url = url
        self.img = img
        self.category = category

SITES = []

with open("blueprints/data/sites.yaml", "r") as file:
    sites = yaml.safe_load(file)
    for site in sites:
        print(site)
        icon = f"https://github.com/walkxcode/dashboard-icons/blob/main/png/{site["icon"]}.png?raw=true"
        site = Site(site["name"], site["url"], icon, site["category"])
        SITES.append(site)