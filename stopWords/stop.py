import json
import help

def init(path):
    jsoncode=help.readTXT(path)
    global stoplist
    stoplist=json.loads(jsoncode)

def isStopWord(word):
    if word[0] in stoplist.keys():
        if word in stoplist[word[0]]:
            return True
    return False

init('stopWordList(gen).txt')
