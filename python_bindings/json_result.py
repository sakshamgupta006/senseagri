import json
data={}
with open('future.json', 'w') as outfile,open("result.txt","r") as f:
    for line in f:
       sp=line.split()
       data.setdefault("Data",[]).append({"MeanModalPrice": sp[3], "Month": sp[1], "Year":sp[2], "SlNo": sp[0]})
    json.dump(data, outfile)