


def steps(num):
    table=[]
    for i in range(num+1):
        if i<=1:
            table.append(0)
        else:
            table.append(-1)


    for i in range(num+1):
        try:
            if table[i+1]==-1:
                table[i+1]=table[i]+1
            else:
                table[i+1]=min(table[i+1],table[i]+1)
        except:
            pass

        try:
            if table[i*2]==-1:
                table[i*2]=table[i]+1
            else:
                table[i*2]=min(table[i*2],table[i]+1)
        except:
            pass
        try:
 
            if table[i*3]==-1:
                table[i*3]=table[i]+1
            else:
                table[i*3]=min(table[i*3],table[i]+1)
        except:
            pass
    return table[num]

print(steps(5))