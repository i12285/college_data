# -*- coding: utf-8 -
from typing import List, Dict
import MeCab
import numpy as np
import gensim
import csv
from gensim import matutils
from sklearn.svm import SVC
from sklearn.model_selection import KFold
from sklearn.metrics import precision_recall_fscore_support, accuracy_score
from tqdm import tqdm
from copy import deepcopy
from sklearn.externals import joblib
from sklearn import linear_model
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report

# 文章をmecabで分かちがきして、名詞・動詞・形容詞の単語一覧を返す
def wakati(text):
    tagger = MeCab.Tagger()
    tagger.parse('')
    node = tagger.parseToNode(text)
    word_list = []
    while node:
        pos = node.feature.split(",")[0]
        if pos in ["名詞"]:
            lemma = node.surface
            word_list.append(lemma)
        node = node.next

    return word_list[1:-1]

# 学習データ
def parse():
    lines = []
    for line in open('train_data.txt', 'r'):
        arr = line.split("\t")
        lines.append(arr)
    return lines


txt=""
csvfile = 'train_data.csv'
f = open(csvfile, "r")
reader = csv.reader(f)
for i, line in enumerate(reader):
    txt += line[2] + "\n"
with open("train_data.txt","w") as f:
    f.write(txt)


wakatis = []
lines = [t[0] for t in parse()]
for line in lines:
    wakatis.append(wakati(line))


df = ""
p_num = -1;
text_1 = ""
feature = ""
csvfile = 'train_data.csv'
list_feature = ["に","へ","まで","から","で","ね","か"]
f = open(csvfile, "r")
reader = csv.reader(f)
for i, line in enumerate(reader):
    df = line[2]
    print(df)
    for j in range(len(wakatis[i])):
        print(wakatis[i])
        c_count=len(wakatis[i][j])
        print(c_count)
        p_num = df.find(wakatis[i][j])
        if p_num != -1:
            num = -(len(df) - p_num - c_count)
            end_num = num + 2 
            text_1 = df[num:end_num]
            print(text_1)
            break
    for k in range(len(list_feature)):        
        print(list_feature[k])
        if(text_1.find(list_feature[k]) != -1):
            feature += list_feature[k] + "\n"
            break
        if(k==6 and text_1.find(list_feature[k]) == -1):
            feature += "0.0" + "\n"
            break
print(feature)

with open("Move_feature.csv","w") as f:
    f.write(feature)




