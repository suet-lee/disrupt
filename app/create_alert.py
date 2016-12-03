from app import app
from twilio.rest import TwilioRestClient
from get_user_alerts import get_user_alerts
import json

def send_sms(country_code, phone_number, service, area, name):
	client = TwilioRestClient(app.ACCOUNT_SID, app.AUTH_TOKEN)
	to_number = country_code + phone_number
	client.messages.create(
	  to=to_number,
	  from_=app.MY_NUMBER,
	  body="New service: "+service+" in "+area+" / "+name
	)

def create_alert(service, area, name):
	data = get_user_alerts(service, area)
	
	for item in data:
		send_sms(item['country_code'], item['phone_number'], service, area, name)

	return 'Alert created'
