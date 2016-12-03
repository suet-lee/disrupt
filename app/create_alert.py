from twilio.rest import TwilioRestClient
import config

client = TwilioRestClient(app.ACCOUNT_SID, app.AUTH_TOKEN)
client.messages.create(
  to=app.TEST_NUMBER,
  from_=app.MY_NUMBER,
  body="Tomorrow's forecast in Financial District, San Francisco is Clear."
)
