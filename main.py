def delim(p):
    flag = True
    a = str(p)
    for i in a:
        if i!='0':
            if p % int(i) != 0:
                flag = False
                break
        else:
            flag = False
            break
    return flag

def DelimInRange(a,b):
    array = []
    for i in range(a,b+1):
        if delim(i):
            array+=[i]
    return array
print(DelimInRange(1,22))