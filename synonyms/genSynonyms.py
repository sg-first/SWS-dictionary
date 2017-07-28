import help
import json

def tonum(id):
    a=id[0:1]
    b=id[1:2]
    c=id[2:4]
    rc=int(c)
    ra=(ord(a)-64)*10000
    rb=(ord(b)-96)*100
    return ra+rb+rc


str=help.readTXT("D:/TCproject/NLP/dic/synonyms(sou).txt")
list=str.split("\n")
jsonlist={} #{now1:{now2:[[word,id]……]}}
now1=""
now2=""

for sen in list:
    interlist=sen.split(",")
    id=tonum(interlist[0])
    word=interlist[1]
    anow1=help.gethead(word)
    anow2=help.gethead2(word)

    if anow1!=now1:
        now1=anow1
    if anow2!=now2:
        now2=anow2

    if not now1 in jsonlist.keys():
        jsonlist[now1]={}
    if not now2 in jsonlist[now1].keys():
        jsonlist[now1][now2]=[]

    jsonlist[now1][now2].append([word,id])

jsoncode=json.dumps(jsonlist,ensure_ascii=False)
help.writeTXT("D:/123.txt",jsoncode)