# -*- coding: utf-8 -*-
import json
import csv
import config
import re
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_API_KEY
CS = config.CONSUMER_API_SELECT_KEY
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
oauth = OAuth1Session(CK, CS, AT, ATS)
endpoint = "https://api.twitter.com/1.1/search/tweets.json"
#   収集条件　変更してね
name_list = ["頭痛","めまい","胃痛","吐き気","しんどい","発熱","動悸","痺れ","下痢","充血","発疹","息切れ","関節痛","吐血"]

set_tweets = []
for i in name_list:
    params = {"q": i , "exclude_replies":"false" , "locale":"ja" , "count":500 , "result_type":"resent"}

    response = oauth.get(endpoint, params=params)
    print(response.url)
    if response.status_code == 200:
        tweets = json.loads(response.text)
        for line in tweets:
            print(line)
            print("**********************:")
    else:
        print("Failed :%d" % response.status_code)

    with open("collecttweets.json", "w") as f:
        json.dump(tweets, f)

    with open('collecttweets.json', 'r') as j:
        json_data = json.load(j)

    text_csv = ""
    for w in json_data['statuses']:
        ## 空白除去
        if "\n" in w['text']:
            w['text'] = ''.join(w['text'].split())
        ## reply・URL除去
        if (("@" in w["text"]) or ("http" in w["text"])): # リプライカット
            pass
        ## csvファイルに書き込み　
        else:
            #   jsonファイルから指定した箇所のみ抽出　変更してね
            text_csv += w["user"]["id_str"] + "," + w["created_at"] + "," + w["text"] + "\n"

    #   必要なデータをCSV形式で保存してる
    with open("collecttweets.csv","a") as f:
        f.write(text_csv)

## 重複ツイート除去 ##
csvfile = "collecttweets.csv"
f = open(csvfile,"r")
list_text = ''.join(list(set([i for i in f.readlines()])))
f.close()
with open("collecttweets.csv","w",encoding = "UTF-8") as f:
    f.write(list_text)

## 読点変換 ##
df = ""
df_2 = ""
csvfile_1 = 'collecttweets.csv'
f_1 = open(csvfile_1, "r")
reader_1 = csv.reader(f_1)
for i, line in enumerate(reader_1):
    text = line[2]
    sen = re.findall(r'[^,]+(?:[、]|$)', text)
    df = ''.join(sen)
    df_2 += '\n' + line[0] + "," + line[1] + "," + str(df)
    f_1.close
with open('collecttweets.csv', 'w') as f:
    f.write(df_2)

