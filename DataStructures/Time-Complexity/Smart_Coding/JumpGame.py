


array=[2,3,1,0,1,4]

def jumpTest(array):
    distance = 0
    current = len(array) - 1
    for i in range(len(array)):
        distance+=1
        if current==0:
            return True

        if array[current-distance]>=distance:
            print((array[current]))
            current-=distance
            distance=0
    return False


print(jumpTest(array))