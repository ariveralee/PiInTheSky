from twilio.rest import TwilioRestClient

account_sid = "account" # Account SID from www.twilio.com/console
auth_token  = "auth_token"  # Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+12673998007",    # Number we are sending it to.
    from_="+12672744736") # Twilio Number

print(message.sid)