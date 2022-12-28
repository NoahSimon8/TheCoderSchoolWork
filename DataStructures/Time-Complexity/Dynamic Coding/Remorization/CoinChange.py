


coins=[1,2,5]
total=11
best=total
def coinchange(current=total):
    global best
    if current==0:
        return 0
    print(current)
    for i in coins:
        if current-i>0:
            round=coinchange(current-i)

            if best>round:
                best=round
                return
    return best

print(coinchange())