

string="abbabbabbaab"

def palendrome(string):
    string=list(string)
    length=1
    for n, i in enumerate(string):
        current=checkPalendromeOdd(string,n,n)
        print(current)
        if current>length:
            length=current
        current=1
    for n, i in enumerate(string):
        pass
    return length

def checkPalendromeOdd(string,x,y,length=1):
    if x != 0 and y != len(string)-1:
        if string[x-1] == string[y+1]:
            length += 2
            return checkPalendromeOdd(string,x-1,y+1,length)
        else:
            return length
    else:
        return length


print("final: "+str(palendrome(string)))