##### check for reverse directly with original ###### 
# def palindrome(string):
#     return string == string[::-1]

# string = input("Enter string:\n")

# result = palindrome(string)
# if result:
#      print("Given string is plaindrome")

# else:
#     print("Given string is not a palindrome")

########################################################

##### Check for individual letter ######################

# def palindrome(string):
#     for i in range(0, int(len(string)/2),1):
#         if string[i] != string[len(string)-1-i]:
#             return False
#     return True
# string = input("Enter string:\n")

# result = palindrome(string)
# if result:
#      print("Given string is plaindrome")

# else:
#     print("Given string is not a palindrome")

############################################################

##### Check for number ######################

def palindrome(num):
    reverse =0
    while(num>0):
        remainder = num%10    
        reverse = remainder + reverse*10
        num = num//10
    return reverse


number = int(input("Enter number:\n"))

reverse = palindrome(number)
if reverse == number:
     print("Given number is plaindrome")
else:
    print("Given number is not a palindrome")

#############################################################