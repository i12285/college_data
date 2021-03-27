import csv
import pandas as pd
import numpy
"""
df =""
df = "今日は池田さんと勉強会の資料を作成した．"
num = df.find("勉強会")
leng = len(df) = 20 
print(leng,num) = 8
"""

#data = ""
df = ""
label = ""
alltext = ""
p = N = n = ""
df1 = ""
num = 0
decide_label = ""
before_p = after_p = 0
before_wc = after_wc = 0
before_text = after_text = ""
last_word = ""
flag = 0
count = count_wc = 0
check_text = ""
before_id = after_id = ""

csvfile = 'train_data.csv'
csvfile1 = 'Tsutsuji_dictionary.csv'
f = open(csvfile, "r")
reader = csv.reader(f)

for i, line in enumerate(reader):
    label = 0.0
    df = line[2]
    

    p_num = df.find("頭痛") 
    if p_num != -1:
        num = -(len(df) - p_num - 2)

    p_num = df.find("めまい") 
    if p_num != -1 and num == 0:
        num = -(len(df) - p_num - 3)
    
    p_num = df.find("胃痛") 
    if p_num != -1 and num == 0: 
        num = -(len(df) - p_num - 2)

    p_num = df.find("吐き気") 
    if p_num != -1 and num == 0:
        num = -(len(df) - p_num - 3)

    p_num = df.find("しんどい") 
    if p_num != -1 and num == 0:
        num = -(len(df) - p_num - 4)

    p_num = df.find("発熱") 
    if p_num != -1 and num == 0:
        num = -(len(df) - p_num - 2)

    p_num = df.find("動悸")
    if p_num != -1 and num == 0:
        num = -(len(df) - p_num - 2)

    p_num = df.find("痺れ")
    if p_num != -1 and num == 0:
        num = -(len(df) - p_num - 2)

    p_num = df.find("下痢")
    if p_num != -1 and num == 0:
        num = -(len(df) - p_num - 2)

    p_num = df.find("充血")
    if p_num != -1 and num == 0:
        num = -(len(df) - p_num - 2)
 
    p_num = df.find("発疹")
    if p_num != -1 and num == 0:
        num = -(len(df) - p_num - 2)
 
    p_num = df.find("息切れ")
    if p_num != -1 and num == 0:
        num = -(len(df) - p_num - 3)

    p_num = df.find("関節痛")
    if p_num != -1 and num == 0:
        num = -(len(df) - p_num - 3)
 
    p_num = df.find("吐血")
    if p_num != -1 and num == 0:
        num = -(len(df) - p_num - 2)

    p_num = df.find("嘔吐")
    if p_num != -1 and num == 0:
        num = -(len(df) - p_num - 2)


    end_num = num + 15
    if end_num > -1:
        end_num = -1

    f1 = open(csvfile1, "r")
    reader1 = csv.reader(f1)
    for i2, line2 in enumerate(reader1):
        text = df[num:end_num]
#        print(text)
        if (text.find(line2[0]) != -1):
#            print(text)
#            print(line2[0])
            after_wc = len(line2[0])
            after_p = text.find(line2[0])
            after_text = line2[0]
            after_id = line2[1]

            count += 1
            if count == 1:
                before_p = after_p
                before_wc = after_wc
                before_text = after_text
                before_id = after_id
            elif after_p <= before_p:
                    before_p = after_p
                   # count_wc += 1
                    if after_p < before_p:
                        before_wc = after_wc
                        before_text = after_text
                        before_id = after_id
                    else:
                        if before_wc <= after_wc:
                            before_wc = after_wc
                            before_text = after_text
                            before_id = after_id

            num = num + before_p + before_wc
            count = 0
        if (len(before_text) != 0) and (check_text != before_text):
            last_word += before_id + ","
#        else:
#            last_word += str(label) + ","
        check_text = before_text
#    last_word += "," + "\n"        
    last_word += "," + "\n"        
    num = 0
#    print("comp")

with open("Tsutsuji_feature.csv","w") as f:
    f.write(last_word)

