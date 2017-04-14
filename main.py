import requests
url='https://github.com/timeline.json'
r=requests.get(url=url)
print(r.raw)
