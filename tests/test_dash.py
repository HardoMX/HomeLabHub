import pytest, shutil

def test_request_dash(client):
    response = client.get("/")
    assert response.request.path == "/"

def test_post_redirect(client):
    # Backup yaml file
    shutil.copyfile("./blueprints/data/settings.yaml", "./blueprints/data/settings-bk.yaml")

    response = client.post("/cms/add/site", follow_redirects=True, data={"title": "Flask", 
                                                                         "url": "https://flask.palletsprojects.com/en/3.0.x/",
                                                                         "description": "Flask documentation",
                                                                         "icon": "flask",
                                                                         "category": "Sites",
                                                                         })
    print(response.data)
    assert len(response.history) == 1
    assert response.request.path == "/"

    # Copy over the backup file to restore original file
    shutil.copyfile("./blueprints/data/settings-bk.yaml", "./blueprints/data/settings.yaml")
