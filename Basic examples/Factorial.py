num = int(input("enter a number"))


def Factorial(n):
    fact = 1
    if n ==1:
        print("Factorial of", n, "is", fact)
    else:
        for i in range(1,n+1):
           fact= fact*i
        print("Factorial of", i, "is", fact)
    

if num <= 0 :
    print("Enter positive number")
else:
    factorial = Factorial(num)
