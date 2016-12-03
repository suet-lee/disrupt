from app import app
from flask import render_template,request
from get_user_alerts import get_user_alerts,save_alert

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/text')
@app.route('/text/<message>')
def text(message='hi'):
    return message

@app.route('/api/post-alert', methods=['POST'])
def post_alert():
    content = request.get_json()
    print content
    save_alert(content)
    return ''

@app.route('/api/get-user-alerts')
def alerts():
	return get_user_alerts()
