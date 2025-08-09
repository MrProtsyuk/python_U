# Simple finding duplicates exercise using dictionaries and loops
def findDup(arr):
    my_map = {}
    for i in arr:
        if i in my_map:
            my_map[i] += 1
        else:
            my_map[i] = 1

    for j in my_map:
        if my_map[j] > 1:
            print(j)

findDup([1,2,2,3,4,5,6,6]) 