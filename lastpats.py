import json
import urllib2
import requests
response = urllib2.urlopen('https://punkapi.com/api/v1/beers/random')
html = response.read()
r=requests.get('https://punkapi.com/api/v1/beers/random')
print r.text
a=raw_input("give us your email to send you the beer !")

def send_simple_message(a):
    return requests.post(
        "https://api.mailgun.net/v3/samples.mailgun.org/messages",
        auth=("api", "key-dff18be32eb51f0e7a82a726258cb573"),
        data={"from": "Excited User <postmaster@sandbox2c7e576cd6a9427cb68517aca98993b1.mailgun.org>",
              "to": ["a"],
              "subject": "beer",
              "text": "r"})
