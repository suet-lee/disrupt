from app import app
from flask import render_template,request,jsonify
from get_user_alerts import get_user_alerts,save_alert,save_service,find_address,search_services
from create_alert import create_alert, send_sms
import json

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/search', methods=['POST'])
def post_results():
	loc = request.form.get('location')
	serv = request.form.get('service')
	data = search_services(loc, serv)
	return render_template('searchpage.html', data={"results": data, "area": str(loc), "service": str(serv)})
	# return jsonify(data)

# @app.route('/search2')
# def post_results2():
# 	data = {"results": [{"name":"Family dentists", "distance": "0.1 miles"}, {"name":"Apple School", "distance": "0.5 miles"}], "area": "shoreditch", "service": "dentist"}
# 	return render_template('searchpage.html', data=data)

@app.route('/sign-up')
def sign_up():
	 return render_template('form.html')

@app.route('/api/post-alert', methods=['POST'])
def post_alert():
	content = request.get_json()
	send_sms(content["country_code"], content["phone_number"], content["service"], content["area"])
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

# Hello ! Jiaee was here