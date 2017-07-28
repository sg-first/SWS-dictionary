import json
import help

def init(path):
    jsoncode=help.readTXT(path)
    global synlist
    synlist=json.loads(jsoncode)

def getid(word):
    now1=help.gethead(word)
    now2=help.gethead2(word)
    if now1 in synlist.keys():
        if now2 in synlist[now1].keys():
            for i in synlist[now1][now2]:
                if i[0]==word:
                    return i[1]
    return -1 #fix:找不到返回什么

def getDistance(word1,word2):
    return abs(getid(word1)-getid(word2))

def isSynonyms(word1,word2,threshold=0):
    return getDistance(word1,word2)<=threshold
