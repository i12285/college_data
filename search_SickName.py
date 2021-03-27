import csv
import pandas as pd
import numpy 

#data = ""
df = ""
label = ""
alltext = ""
df1 = "" 
df2 = ""
flag = 0

csvfile = 'train_data.csv'
#csvfile1 = 'body_part.csv'
csvfile1 = 'MedicalNote.csv'

f = open(csvfile, "r")
reader = csv.reader(f)
 
for i, line in enumerate(reader):
    df = line[2]
    f1 = open(csvfile1, "r")
    reader1 = csv.reader(f1)
    for ii, line1 in enumerate(reader1):
        df1 = line1[0]

        if (df.find(df1) != -1):
            df2 += "1.0" + "\n"
            flag = 1
            break

    if flag == 0:
        df2 += "0.0" + "\n"

    flag = 0

with open("Sick_feature.csv","w") as f:
    f.write(df2)    
