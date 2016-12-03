from contextlib import closing
from app import app
import config
import MySQLdb
import MySQLdb.cursors
from flask import jsonify

def get_user_alerts():
	db = MySQLdb.connect(host=app.DB_HOST, user=app.DB_USER, passwd=app.DB_PASSWD, db=app.DB_NAME, cursorclass=MySQLdb.cursors.DictCursor)
	with closing(db.cursor()) as cursor:
		cursor.execute("SELECT * FROM user_alerts WHERE active = 1")
		data = jsonify(cursor.fetchall())
	return data

def save_alert(content):
	db = MySQLdb.connect(host=app.DB_HOST, user=app.DB_USER, passwd=app.DB_PASSWD, db=app.DB_NAME, cursorclass=MySQLdb.cursors.DictCursor)
	with closing(db.cursor()) as cursor:
            cursor.execute(
                    "INSERT INTO user_alerts(country_code, phone_number, area, service) VALUES (%s,%s,%s,%s)", 
                    (content['country_code'], content['phone_number'], content['area'], content['service']))
            db.commit()
