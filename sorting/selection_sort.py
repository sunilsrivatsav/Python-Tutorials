
list = [23,8,1,5,9,1,18,65]

def selectionsort(list):
    ### outer loop goes from n, n-1, n-2, ....
    for i in range(len(list)-1):
        minpos = i
        ### finds minimum number and pushes to left corner 
        for j in range(i,len(list)):
            if list[j]<list[minpos]:
                minpos = j
        ### Swaps at end of first iteration
        temp = list[i]
        list[i] = list[minpos]
        list[minpos] = temp
    print(list)

selectionsort(list)