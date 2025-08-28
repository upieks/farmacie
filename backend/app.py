# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from models import get_session, SES, Healthcare, init_db


app = Flask(__name__)
CORS(app)
init_db()


@app.route("/api/v1/ses")
def ses_lookup():
pc = request.args.get("postcode")
year = int(request.args.get("year", 2023))
s = get_session()
rec = s.query(SES).filter_by(postcode=pc, year=year).first()
s.close()
if not rec:
return jsonify({"error": "not found"}), 404
return jsonify(rec.data)


@app.route("/api/v1/healthcare")
def healthcare_lookup():
pc = request.args.get("postcode")
year = int(request.args.get("year", 2023))
s = get_session()
rec = s.query(Healthcare).filter_by(postcode=pc, year=year).first()
s.close()
if not rec:
return jsonify({"error": "not found"}), 404
return jsonify(rec.data)


@app.route("/api/v1/ping")
def ping():
return {"status": "ok"}