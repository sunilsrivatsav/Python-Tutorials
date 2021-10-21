list = [23,8,1,5,9,1,18,65]

pos = -1
def linearsearch(n):

    for i,num in enumerate(list):
        if num==n:
            globals()['pos'] = i
            return True
    return False

n = 64
if linearsearch(n):
    print("found at : ", pos)
else:
    print("not found")