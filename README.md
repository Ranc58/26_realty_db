# Real Estate Site
Test model of site.\
Getting data about flats in JSON format, put it in SQLite DB, and then displayed data to site.

# How to install
1. Recomended use venv or virtualenv for better isolation.\
   Venv setup example: \
   `$ python3 -m venv myenv`\
   `$ source myenv/bin/activate`
2. Install requirements: \
   `pip3 install -r requirements.txt` (alternatively try add `sudo` before command)

# How to use
Primarily, you need to create DB and make first JSON load operation.\
Script for work with DB: `db_operations.py`\
Command for create DB: `$ python3 db_operations.py -c`\
Command for update DB: `$ python3 db_operations.py -u`\
After DB is created and updated, run flask server: `$ python3 server.py`\
And go to site: `http://127.0.0.1:5000/` 

**Some useful info**
1) Each time you upload new data to DB, old records get status `active: False` and no longer displayed on the site, but saved in DB.
2) Button `Только новостройки` on site displayed only new flats(not older than 2 years).
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
