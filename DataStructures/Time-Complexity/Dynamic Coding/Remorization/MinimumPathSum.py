#
#
    # array=[[1,3,1],
    #        [1,5,2],
    #        [4,2,2]]
#
# def path(x=0,y=0):
#     end=[False,False]
#
#     if x==len(array)-1:
#         end[0]=True
#     if  y == len(array) - 1:
#         end[1]=True
#
#     if end==[True,True]:
#         return array[y][x]
#
#
#     if end==[False,True]:
#         return path(x+1,y)+array[y][x]
#     elif end==[True,False]:
#         return path(x,y+1)+array[y][x]
#     else:
#         return min(path(x+1,y),path(x,y+1))+array[y][x]
#
# print(path())
array = [[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],
        [9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],
        [8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],
        [6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],
        [7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],
        [9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],
        [1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],
        [3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],
        [1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],
        [5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],
        [2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],
        [0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]
# array =[[1,3,7,1],
#        [1,5,2,0],
#        [4,2,9,4],
#        [0,1,8,1]]
# array=[[31, 100, 65, 12, 18 ],
#        [10, 13,  47, 157,6 ],
#        [100,113, 174,11, 33 ],
#        [88, 124, 41, 20, 140 ],
#        [99, 32,  111,41, 20 ]]

dict = {}

def path(x=0, y=0):
    end = [False, False]

    if x == len(array[0]) - 1:
        end[0] = True
    if y == len(array) - 1:
        end[1] = True
    if str(x)+str(y) not in dict:
        if end == [True, True]:
            dict[str(x) + str(y)] = array[y][x]
            return array[y][x]

        if end == [False, True]:
            dict[str(x) + str(y)] = path(x + 1, y) + array[y][x]
            return dict[str(x) + str(y)]
        elif end == [True, False]:
            dict[str(x) + str(y)] = path(x, y + 1) + array[y][x]
            return dict[str(x) + str(y)]
        else:
            dict[str(x) + str(y)] = min(path(x + 1, y), path(x, y + 1)) + array[y][x]
            return dict[str(x) + str(y)]
    return dict[str(x) + str(y)]

print(path())