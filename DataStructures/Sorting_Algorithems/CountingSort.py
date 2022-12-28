


def CountingSort(lst):
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
    for i in lst:
        sorted[sortindex[i]]=i
        sortindex[i]+=1



    return sorted




