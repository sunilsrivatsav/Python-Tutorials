list = [1,6,9,15,34,55,78]
## list should be sorted for binary search
list.sort()

num_pos = -1
def binarysearch(n,list):
    L = 0
    U = len(list)-1
    while(L<=U):
        #### calculate mid and compare the value
        mid = (L+U)//2
        if list[mid]==n:
            globals()['num_pos']=mid
            return True
        else:
            ####  move the lower bound right
            if list[mid]<n:
                L = mid+1
            ##### move the upper bound left
            else:
                U=mid-1
    return False

n = 46
if binarysearch(n,list):
    print("found at: ", num_pos)
else:
    print("not found")