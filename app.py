# pipenv install twilio
from twilio.rest import Client
from config import account_sid, auth_token

client = Client(account_sid, auth_token)

client.messages.create(
    to="+4407529186453",
    from_="+17405701114",  # the twilio number you created
    body="A message from Kyra...(Beta test for my latest project lol)"
)

# call.date_created()
