import requests
import json
import time
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

nltk.download('all')
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

        sia = SIA()
    pos_list = []
    neg_list = []
    for post in data_all:
        res = sia.polarity_scores(post['data']['title'])

        if res['compound'] > 0.2:
            pos_list.append(post['data']['title'])
        elif res['compound'] < -0.2:
            neg_list.append(post['data']['title'])

    with open("pos_crypto.txt", "w", encoding='utf-8',
        errors='ignore') as f_pos:
        for post in pos_list:
            f_pos.write(post + "\n")

    with open("neg_crypto.txt", "w", encoding='utf-8',
          errors='ignore') as f_neg:
        for post in neg_list:
            f_neg.write(post + "\n")