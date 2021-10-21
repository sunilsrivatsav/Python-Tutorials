list = [1,6,9,15,34,55,78]
list.sort()

position=-1
def binarysearch(n,list):
    Lower = 0
    Upper = len(list)-1
    while(Lower<=Upper):
        #### calculate mid and compare the value
        mid = (Lower+Upper)//2
        if list[mid]==n:
            globals()['position']=mid
            return True
        else:
            ####  move the lower bound right
            if list[mid]<n:
                Lower = mid+1
            ##### move the upper bound left
            else:
                Upper=mid-1
    return False

n = 46
if binarysearch(n,list):
    print("found at: ", position)
else:
    print("not found")