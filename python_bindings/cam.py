import csv
import json

data={}
count =0
with open('news.json', 'w') as outfile,open("news.txt","r") as f:
    for line in f:
        if count==0:
            p = line
        if count==1:
            q = line
        if count == 2:
            r = line
        if count==3:
            s= line
        if count==4:
            data.setdefault("Data",[]).append({"link": p, "title": q, "src":r, "p": s})
            count =0
            continue
        count +=1
    json.dump(data, outfile)