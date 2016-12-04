from app import app
from flask import render_template,request,jsonify
from get_user_alerts import get_user_alerts,save_alert,save_service,find_address,search_services
from create_alert import create_alert

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/search', methods=['POST'])
def post_results():
    print request.form
    loc = request.form.get('location')
    serv = request.form.get('service')
    data = search_services(loc, serv)
    return jsonify(data)


@app.route('/api/post-alert', methods=['POST'])
def post_alert():
    content = request.get_json()
    print content
    save_alert(content)
    return ''

@app.route('/api/post-service', methods=['POST'])
def post_service():
    content = request.get_json()
    print content
    save_service(content)
    return ''

@app.route('/api/get-address/<coords>', methods=['GET'])
def get_address(coords):
    return find_address(coords)

@app.route('/api/get-user-alerts/<service>/<area>')
def alerts(service, area):
	return jsonify(get_user_alerts(service, area))

# @app.route('/create-alert/<service>/<area>/<name>')
# def route_create_alert(service, area, name):
# 	return create_alert(service, area, name)
