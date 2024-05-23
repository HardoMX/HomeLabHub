# Developer documentation for HomeLabHub

## Table of contents
1. [Introduction](#introduction)
2. [Technical Specification and Design](#technical-inspection-and-design)
3. [Architecture](#architecture)
4. [Guidelines and Standards](#guidelines-and-standards)
5. [Testing](#testing)
6. [Accessibility](#accessibility)
7. [Troubleshooting and FAQs](#troubleshooting-and-faqs)
8. [Further Reading](further-reading)
9. [Roadmap](#roadmap)
10. [Feedback](#feedback)

--- 

## Introduction
HomeLabHub serves as, wait for it..., the hub for your homelab. It is a simple website that lets you add links to websites to a page.
It will also be able to have some integration with the host server and services like proxmox.

This project was started as a school project and is made using python and Flask.

### Setup
1. Clone the repo
2. Create an environment with `python -m venv ./` and activate it with `source bin/activate`
3. Install the required packages using `pip install -r config/requirements.txt`
4. Start the app with `python app.py`

--- 

## Technical Specification and Design
This project uses:
- Python (Language)
- Flask (Web server framework)
- PyOWM (Weather API comms)
- PyYAML (YAML parsing)

--- 

## Architecture
### Program calling structure
```markdown
app.py
 |
 +-factory.py
    |
    +-dashboard.py
    |  |
    |  +-api.py
    |  |
    |  +-settings.py
    |  |  |
    |  |  +-settings.yaml
    |  |
    |  +-dashboard.html
    |     |
    |     +-index.html
    |     |  |
    |     |  +-index.css
    |     |  |
    |     |  +-time.js
    |     |  |
    |     |  +-modal.js
    |     |
    |     +-dashboard.css
    |
    +-cms.py
       |
       +-api.py
       |
       +-settings.py
       |  |
       |  +-settings.yaml
       |
       +-settings.html
          |
          +-index.html
          |  |
          |  +-index.css
          |  |
          |  +-time.js
          |  |
          |  +-modal.js
          |
          +-settings.css
```


**File structure**
```markdown
`/src` (just `/HomeLabHub` when using from the `main` branch)
 |
 +-`.gitignore`
 |
 +-`LICENCE`
 |
 +-`README.md`
 |
 +-`.git/`
 |
 +-`docs/`
 |  |
 |  +-`developer_documentation.md`
 |  |
 |  +-`user_documentation.md`
 |
 +-`tests/`
 |  |
 |  +-`test.py`
 |  |
 |  +-`<all same as /src/>`
 |
 +-`src/`
    |
    +-`app.py`
    |
    +-`factory.py`
    |
    +-`blueprints/`
    |  |
    |  +-`__init__.py`
    |  |
    |  +-`cms.py`
    |  |
    |  +-`dashboard.py`
    |  |
    |  +-`data/`
    |     |
    |     +-`__init__.py`
    |     |
    |     +-`api.py` (create yourself)
    |     |
    |     +-`settings.yaml`
    |     |
    |     +-`settings.py`
    |
    +-`templates/`
    |  |
    |  +-`index.html`
    |  |
    |  +-`dashboard.html`
    |  |
    |  +-`settings.html`
    |
    +-`static/`
       |
       +-`css`
       |  |
       |  +-`index.css`
       |  |
       |  +-`dashboard.css`
       |  |
       |  +-`settings.css`
       |
       +-`images/`
       |  |
       |  +-`backgrounds/`
       |  |  |
       |  |  +-`default.png`
       |  |
       |  +-`weather-icons/`
       |     |
       |     +-`01d.svg`
       |     |
       |     +-`01n.svg`
       |     |
       |     +-`02d.svg`
       |     |
       |     +-`02n.svg`
       |     |
       |     +-`03d.svg`
       |     |
       |     +-`03n.svg`
       |     |
       |     +-`04d.svg`
       |     |
       |     +-`04n.svg`
       |     |
       |     +-`09d.svg`
       |     |
       |     +-`09n.svg`
       |     |
       |     +-`10d.svg`
       |     |
       |     +-`10n.svg`
       |     |
       |     +-`11d.svg`
       |     |
       |     +-`11n.svg`
       |     |
       |     +-`13d.svg`
       |     |
       |     +-`13n.svg`
       |     |
       |     +-`50d.svg`
       |     |
       |     +-`50n.svg`
       |     |
       |     +-`blizzard.svg`
       |     |
       |     +-`blowing-sand-at-night.svg`
       |     |
       |     +-`dust.svg`
       |     |
       |     +-`heavy-rain.svg`
       |     |
       |     +-`heavy-snow.svg`
       |     |
       |     +-`jansa.svg`
       |     |
       |     +-`light-rain.svg`
       |     |
       |     +-`light-snow.svg`
       |     |
       |     +-`moderate-snow.svg`
       |     |
       |     +-`rainstorm.svg`
       |     |
       |     +-`unknown.svg`
       |
       +-`js/`
          |
          +-`modal.js`
          |
          +-`time.js`
```

--- 

## Guidelines and Standards
Just follow PEP8 and you're fine :)

## Testing
There are some simple tests in `HomeLabHub/tests` you can run with the `pytest` command. These tests test if the main page is accessible, that the post works, and that you get redirected correctly.

## Accessibility
Follow standard HTML recommendations, if you find something that's not up to code, fix it and make a pull request.

## Troubleshooting and FAQs
#### Q: The application won't start, what should I do?
     **A: Make sure all dependencies are installed**

#### Q: The application still won't start
     **A: Check if there is something wrong with the YAML file**

#### Q: There is something wrong with the YAML file
     **A: You can see a correct YAML file in this repo, copy it and change to the sites you need**

#### Q: Something still won't work
     **A: Open a new [issue](https://github.com/HardoMX/HomeLabHub/issues) on GitHub**

---

## Further Reading
- [Flask documentation](https://flask.palletsprojects.com/en/3.0.x/)
- [PyOWM documentation](https://pyowm.readthedocs.io/en/latest/)
- [YAML syntax](https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html)

## Roadmap
**Features I want to add**
- Database instead of yaml for sites
- User based sites
- Websocket for weather info
- System info card
- Proxmox and other services integration

## Feedback
If you want to leave feedback, create a new [issue](https://github.com/HardoMX/HomeLabHub/issues) on GitHub
