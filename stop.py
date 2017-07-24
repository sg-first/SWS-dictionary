import json
import help

def init(path):
    jsoncode=help.readTXT(path)
    global stoplist
    stoplist=json.loads(jsoncode)

def isStopWord(word):
    nowhead=help.gethead(word)
    for k in stoplist.keys():
        if k==nowhead:
            for i in stoplist[k]:
                if i==word:
                    return True
            return False #循环完了都没有
