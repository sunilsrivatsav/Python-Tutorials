
list = [23,8,1,5,9,1,18,65]

def bubblesort(list):
    ## outer loop goes from n, n-1, n-2, ....
    for i in range(len(list)-1,0,-1):
        ##Inner loop for comparing two numbers
        ## finds max number and pushes to right corner
        for j in range(i):
            if list[j]>list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    print(list)

bubblesort(list)