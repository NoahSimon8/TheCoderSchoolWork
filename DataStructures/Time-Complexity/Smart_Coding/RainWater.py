


# O(n)
# Mine (issue, but close)


# # array=[0,2,0,3,0,0,1,3,2,1,2,1]
array=[0,1,0,2,1,0,1,3,2,1,2,1]
# #1,1,2,1,1,2,1,2
def rain():
    water=0
    Peak=0
    currentHole=0
    for n,i in enumerate(array):
        if i>=Peak:
            water+=currentHole
            Peak=i
            print(currentHole)
            currentHole=0
        currentHole+=Peak-i

    return water

print(rain())



# Alex's (works


#O(n)

def trapping_rain_water(array):
    area = 0
    left = 0
    right = len(array)-1
    lmax = 0
    rmax = 0

    while left < right:
        if array[left] < array[right]:          # Step 1: check if left less than right
            if array[left] > lmax:              # Step 2: change to new lmax if can
                lmax = array[left]
            else:                               # Step 3: else calc area
                area += lmax - array[left]

            left += 1                           # Step 4 increment left
        else:
            if array[right] > rmax:
                rmax = array[right]
            else:
                area += rmax - array[right]
            right -= 1

    return area


print(trapping_rain_water([0,1,0,2,1,0,1,3,2,1,2,1]))


'''
|        Rain Water
|
|               @
|       @ # # # @ @ # @
|   @ # @ @ # @ @ @ @ @ @ 
-----------------------------
  0 1 0 2 1 0 1 3 2 1 2 1
'''



