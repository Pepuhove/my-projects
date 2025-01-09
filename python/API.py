import requests
response=requests.get(url='http://api.open-notify.org/iss-now.json')
print(response.status_code)
if response.status_code==200:
    raise Exception('OK')
elif response.status_code==404:
    raise Exception('Not found')
else:
    raise Exception('None')