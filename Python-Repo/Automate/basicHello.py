import requests

user_agent = {
    'name': 'Practice bots',
    'email': 'emailaddress@gmail.com'
}
header = {'User-Agent': 'python-requests (compatible; {0}; {1})'.format(user_agent['name'], user_agent['email'])}
res = requests.get("https://xkcd.com/robots.txt", headers = header)
try:
    res.raise_for_status()
except Exception as ex:
    print("There was a problem : %S" %(ex))
print("Status code is {0}".format(res))
print(res.text)