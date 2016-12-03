from app import app
from flask import render_template
from get_user_alerts import get_user_alerts

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/text')
@app.route('/text/<message>')
def text(message='hi'):
	return message

@app.route('/api/get-user-alerts')
def alerts():
	return get_user_alerts()
