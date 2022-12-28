



# i=0
# total=0
# while i<100:
#     i+=1
#     if i%2==0:
#         total+=i
# print(total)

def even(start,end,total):
    if start==end:
        return total
    else:

        start+=1
        # print(start)
        if start%2==0:
            total+=start
            # print(total)
        return even(start,end,total)


print(even(0,100,0))