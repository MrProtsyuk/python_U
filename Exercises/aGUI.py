def picture(arr):
    for i in arr:
        output = ""
        for j in i:
            if j == 0:
                output += " "
            if j == 1:
                output += "*"       
        print(output)
    
    return

picture([
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,1,1,1,1,1,0],
    [0,0,1,1,1,0,0],
    [0,0,0,1,0,0,0]
])