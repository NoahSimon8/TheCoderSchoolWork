
#O(n) time complex  and O(1) space complexity

array = [1,4,6,4,2,1,6,8]

for i in array:
    if array[abs(i)-1]<0:
        print(abs(i))
        break
    else:
        array[abs(i)-1]*=-1