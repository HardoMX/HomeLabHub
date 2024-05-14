from factory import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique = True)
    sites_list = db.Column(db.Integer, db.ForeignKey('sitelist.id'))

    def __repr__(self):
        return f"{self.username}"

class Site(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), index=True)
    url = db.Column(db.String(50), index=True)
    icon = db.Column(db.String(50), index=True)
    n = db.Column(db.Integer, index=False, unique=False)

    def __repr__(self):
        return f"Title: {self.title}, url: {self.url}, icon: {self.icon}"

class Item(db.Model): # What is this?
    id = db.Column(db.Integer, primary_key=True)
    site_id = db.Column(db.Integer, db.ForeignKey('site.id'))
    sites_list = db.Column(db.Integer, db.ForeignKey('sitelist.id'))

    def __repr__(self):
        return f"{Site.query.get(self.site_id)}"

class Sitelist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True)
    items = db.relationship('Item', backref='sitelist', lazy='dynamic')

    def __repr__(self):
        return f"Sitelist {self.id}"

