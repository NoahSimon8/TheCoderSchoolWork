#
#
# def steps(num):
#
#     if num==1:
#         return 0
#     elif num%3==0 and num%2==0:
#         return min(steps(num/3), steps(num/2), steps(num-1))+1
#     elif num%3==0:
#         return min(steps(num/3), steps(num-1))+1
#     elif num%2==0:
#         return min(steps(num/2), steps(n  um-1))+1
#     else: return steps(num-1)+1
#
# print(steps(400))
# #

dic={}

def steps(num):

    if num==1:
        return 0
    if num not in dic:
        if num%3==0 and num%2==0:
            dic[num] = min(steps(num/3), steps(num/2), steps(num-1))+1
        elif num%3==0:
            dic[num] = min(steps(num/3), steps(num-1))+1
        elif num%2==0:
            dic[num] = min(steps(num/2), steps(num-1))+1
        else:
            dic[num] = steps(num-1)+1
    return dic[num]

print(steps(2000))