class Site:
    def __init__(self, name, url, img):
        self.name = name
        self.url = url
        self.img = img
        
youtube = Site("YouTube", "https://www.youtube.com", "https://github.com/walkxcode/dashboard-icons/blob/main/png/youtube.png?raw=true")
amazon = Site("Amazon", "https://amazon.com", "https://github.com/walkxcode/dashboard-icons/blob/main/png/amazon.png?raw=true")

sites = []
sites.append(youtube)
sites.append(amazon)