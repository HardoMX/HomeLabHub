# User documentation for HomeLabHub

## Table of Contents
1. **[Installation](#installation)**
2. **[User Manual](#user-manual)**
3. **[FAQs and Troubleshooting](#faqs-and-troubleshooting)**
4. **[Contact](#contact)**

---

## 1. Installation
### Dependencies
Install python, either using an install file, or with a package manager. 

The other dependencies can be installed with `pip install -U -r ./config/requirements.txt`, or through a package manager like `pacman` or `apt`
- Flask 
- pyowm
- pyyaml
- setuptools
- pytest

### Installation
clone the github repo with `git clone https://github.com/hardomx/homelabhub`

### Running
1. move into it using `cd HomeLabHub`
2. start the application with `python app.py`

---

## 2. User Manual
### Accessing the application
After starting the application you can access it through a browser.
By default the website is reached at `<server-ip>:300`, if you run it on the same computer as you're using, it will be at `127.0.0.1:3000`

### UI
Much of the UI can be configured, see [configuring](#configuring)

#### Dashboard
- On the left side of the screen is a clock, weather information, and in the future there will be some info about system resources. 
- The main area is segmented into categories.
    - Each category has a title and a list of sites under it. In the future categories will be collapsible. 
    - Sites have an icon and a title. When hovered, additional info is displayed in a tooltip. 
- A button to add sites. This opens a window to add new sites to the app
    - Title (required): Write a name for your link
    - URL (required): Write the url for your link, has to be a valid url
    - Description (optional): Write a description for your link, shows up as a tooltip
    - Icon (required): Add an icon, see more at [configuring](#configuring)
    - Category: Choose a category to add the site to, see more at [configuring](configuring)
- A link to the settings page

#### Settings
- Has the same part on the left
- Edit settings file. This controls the entire site, so be careful. See more at [configuring](configuring)
- Upload background, upload a background image
- Return to dashboard

### Configuring
All configuration is done through the `settings.yaml` file. To find how to write yaml, see [Ansible's syntax guide](https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html).
When adding sites to the file, order doesn't matter, the yaml site renders them in the correct category anyways. 

You can change the settings in three ways:
1. Through the "add site" form on the dashboard page. This is the most safe option, as the program does the syntax for you. However, this can only add sites, not remove them ocr change any other settings. To do that you can
2. Edit the file from the settings page. Here you can change background image, location, categories, and sites. This file is not validated in any way, if you do something wrong things *WILL* break, luckily, most things except weather and links should still work, so you can fix it.
3. The third way is to edit the yaml file directly, this is essentially the same as option 2, but you need physical or remote access to the server. 

#### YAML options
- `background:` set the filename of the background image. Images need to be in `static/images/backgrounds`, images uploaded through the site are always stored correctly.
- `location:` set the location for weather information, e.g `stockholm,SE` or `london,GB`
- `gategories:` a list of all the categories you want, every category needs to start with `- `
- `sites:` a list of sites, every site needs to start with `- name: ` and following new lines need corresponding keys, start a new site object with `- `

---

## 3. FAQs and Troubleshooting
#### Q: The application won't start, what should I do?
     **A: Make sure all dependencies are installed**

#### Q: The application still won't start
     **A: Check if there is something wrong with the YAML file**

#### Q: There is something wrong with the YAML file
     **A: You can see a correct YAML file in this repo, copy it and change to the sites you need**

#### Q: Something still won't work
     **A: Open a new [issue](https://github.com/HardoMX/HomeLabHub/issues) on GitHub**

---

## 4. Contact
If you want a feature added, or any help, make an [issue](https://github.com/HardoMX/HomeLabHub/issues) on GitBub.
