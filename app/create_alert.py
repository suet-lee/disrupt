from twilio.rest import TwilioRestClient
# put your own credentials here

client = TwilioRestClient(app.ACCOUNT_SID, app.AUTH_TOKEN)
client.messages.create(
  to="+447749068166",
  from_="+441457597079",
  body="Tomorrow's forecast in Financial District, San Francisco is Clear."
)
