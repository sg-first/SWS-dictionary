def readTXT(path):
    return open(path,'r').read()

def printlist(list,sep=''):
    print(sep.join(list))

def writeTXT(path,content):
    open(path, 'w').write(content)

def gethead(str):
    return str[0:1]