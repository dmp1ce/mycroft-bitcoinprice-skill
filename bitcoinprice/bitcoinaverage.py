import requests

try:
    r = requests.get("http://apiv2.bitcoinaverage.com/indices/local/ticker/btcusd") 
    print("The Bitcion daily average is %s USD." %(r.json()['averages']['day']))
except:
    print("Something went wrong in getting bitcoinaverage request")
