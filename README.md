# README.md
# Farmacie


Farmacie is a PythonAnywhere‑hosted SaaS providing socioeconomic (SES) and healthcare cost data per postcode in the Netherlands.


## Modules
- **SES**: socioeconomic indicators (from CBS Open Data)
- **Healthcare**: healthcare cost per postcode


## Tech stack
- Flask API (backend)
- SQLAlchemy + MySQL (storage)
- Leaflet (frontend map)
- Data sources: CBS Open Data (StatLine), PDOK Geo services


## Setup
```bash
# clone repo
git clone https://github.com/yourname/farmacie.git
cd farmacie/backend


# create virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


# set DATABASE_URL in .env or environment
export DATABASE_URL="mysql+pymysql://USER:PASSWORD@HOST/DBNAME"


# run app
flask --app app run --debug
```


Visit http://127.0.0.1:5000/api/v1/ping to test.


## Deployment on PythonAnywhere
1. Clone repo on PA.
2. Create MySQL DB on Databases tab.
3. Set `DATABASE_URL` in environment.
4. Configure webapp → point WSGI to `backend/wsgi.py`.
5. Reload webapp.
 
