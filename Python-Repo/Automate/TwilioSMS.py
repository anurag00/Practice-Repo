from twilio.rest import Client
import time

passFile = open(r'G:\Pycode\Automate\API\TwilioAPI.txt','r')
TwilioUser = passFile.read().split()

client = Client(TwilioUser[0],TwilioUser[1])
fromNum = TwilioUser[2]
toNum = TwilioUser[3]
message = client.api.account.messages.create(
    to = toNum,
    from_ = fromNum,
    body = "Hey Man, just wanted to say that you rock bro"
)

print("ID : ", message.sid)
print("To : ", message.to)
print("From : ", message.from_)
print("Body : ", message.body)
print("Status : ", message.status)

for x in range(10):
    time.sleep(1)

messageUpdate = client.messages(message.sid).fetch()
print("Status : ", messageUpdate.status)