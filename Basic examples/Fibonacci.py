num = int(input("enter a number"))


def fibonacci(n):
    a= 0
    b= 1
    if n ==1:
        print(a)
    else:
        #### counter to check the last term
        counter = 0
        while(counter<num):
            print(a)
            c=a+b
            a=b
            b=c
            counter += 1

if num <= 0 :
    print("Enter positive number")

else:
    fibonacci(num)