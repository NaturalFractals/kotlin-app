import requests
import json
import time
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

# Set your header according to the form below
# :: (by /u/)

# Add your username below
hdr = {'User-Agent': 'windows:r/CryptoCurrency.single.result:v1.0' +
       '(by /u/)'}
url = 'https://www.reddit.com/r/CryptoCurrency/.json'
req = requests.get(url, headers=hdr)
json_data = json.loads(req.text)
posts = json.dumps(json_data['data']['children'], indent=4, sort_keys=True)
print(posts)

data_all = json_data['data']['children']
num_of_posts = 0
while len(data_all) <= 100:
    time.sleep(2)
    last = data_all[-1]['data']['name']
    url = 'https://www.reddit.com/r/CryptoCurrency/.json?after=' + str(last)
    req = requests.get(url, headers=hdr)
    data = json.loads(req.text)
    data_all += data['data']['children']
    if num_of_posts == len(data_all):
        break
    else:
        num_of_posts = len(data_all)