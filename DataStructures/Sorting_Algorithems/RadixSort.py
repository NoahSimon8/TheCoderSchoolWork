from CountingSort import*
from random import*
def RadixSort(lst):
    index=1
    maximum=max(lst)
    while maximum%(10**(index-1))!=maximum:
        digits=getdigits(lst.copy(),index)
        lst=CountingSort(digits,lst)
        index+=1
    return lst

def getdigits(digits,index): #index right to left
    for i in range(len(digits)):
        digits[i]=digits[i]%(10**index)//(10**(index-1))
    return digits



def CountingSort(lst,originals):
    size=max(lst)
    occurrences=[0 for i in range(size+1)]

    for i in lst:
        occurrences[i]+=1
    # print(occurrences)

    sums=occurrences
    for i in range(len(sums)-1):
        sums[i+1]+=sums[i]
    # print(sums)

    shifted=[0]
    shifted+=sums
    shifted.pop()
    # print(shifted)

    sortindex=shifted
    sorted=[0.5 for i in range(len(lst))]

    for i in range(len(lst)):
        sorted[sortindex[lst[i]]]=originals[i]
        sortindex[lst[i]]+=1



    return sorted


print(RadixSort([randint(0,1000) for i in range(500)]))
# print(RadixSort(["a","b","d","c"]))