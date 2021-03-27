import csv
import pandas as pd
import numpy

df = ""
label = ""
alltext = ""
p = N = n = ""
df1 = ""
count=0
set_count=0

csvfile = 'Tsutsuji_feature.csv'
f = open(csvfile, "r")
reader = csv.reader(f)

for i, line in enumerate(reader):
     if(i==0):
         count=len(line)
     if(len(line)>count):
         count=len(line)
count=count-2

csvfile = 'Tsutsuji_feature.csv'
f = open(csvfile, "r")
reader = csv.reader(f)

for ii, lines in enumerate(reader):
    set_count=(len(lines))-2
    for j in range(set_count):
        df1 += lines[j] + ","
    for k in range(count-set_count):
        if(k==count-set_count-1):
            df1 += "0.0"
        else:
            df1 += "0.0" + ","
    df1 += "\n"

with open("Tsutsuji_feature.csv","w") as f:
	f.write(df1)
