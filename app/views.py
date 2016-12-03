from app import app
from flask import render_template, jsonify
from get_user_alerts import get_user_alerts
from create_alert import create_alert

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/text')
@app.route('/text/<message>')
def text(message='hi'):
	return message

@app.route('/api/get-user-alerts/<service>/<area>')
def alerts(service, area):
	return jsonify(get_user_alerts(service, area))

@app.route('/create-alert/<service>/<area>/<name>')
def route_create_alert(service, area, name):
	return create_alert(service, area, name)
