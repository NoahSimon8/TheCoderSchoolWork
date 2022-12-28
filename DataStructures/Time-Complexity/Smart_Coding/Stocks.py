

array=[7,2,1,5]

def stock():
    lowest=array[0]
    profit=0
    for i in array:
        lowest = min(i, lowest)
        profit=max(i-lowest,profit)
    return profit

print(stock())

