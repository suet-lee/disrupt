from twilio.rest import TwilioRestClient
# put your own credentials here
import config
import MySQLdb

db = MySQLdb.connect(host=app.DB_HOST, user=app.DB_USER, passwd=app.DB_ROOT, db=app.DB_NAME)




client = TwilioRestClient(app.ACCOUNT_SID, app.AUTH_TOKEN)
client.messages.create(
  to=app.TEST_NUMBER,
  from_=app.MY_NUMBER,
  body="Tomorrow's forecast in Financial District, San Francisco is Clear."
)
