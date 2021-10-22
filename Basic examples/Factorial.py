######## Basic formulation ##################
num = int(input("enter a number"))


def Factorial(n):
    fact = 1
    if n ==1:
        print("Factorial of", n, "is", fact)
    else:
        for i in range(1,n+1):
           fact= fact*i
        print("Factorial of", i, "is", fact)
    

if num < 0 :
    print("Enter positive number")
elif num == 0:
    print("Factorial of", num, "is 1")
else:
    Factorial(num)

##############################################
############# Recurssion #####################

# def Factorial(n):
#     if n==1:
#         return n
#     else:
#         return n*Factorial(n-1)

# num = int(input("enter a number"))
# if num < 0 :
#     print("Enter positive number")
# elif num == 0:
#     print("Factorial of", num, "is 1")
# else:
#     factorial = Factorial(num)
#     print("Factorial of", num, "is:",factorial)

###################################################
