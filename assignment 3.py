


#Assignmnets :3
#1 write a function to check whether input string is palindrome
#2 write a function to find the factorial of  number
#3 write a function to the fibonacci series of the number

#Answers
"""
#1 write a function to check whether input string is palindrome
a=input("enter the string").upper()
def checkPalindrome(a):
    if a==a[::-1]:

        print("a is palindrome")
    else:

        print("a not palindrome")
    return

checkPalindrome(a)



#2 first method write a function to find the factorial of  number
#a=int(input("enter the number"))
def factorial(a):
    fact=1
    for i in range(1,a+1):
        if a==0:
            print(1)
        else:
            fact=fact*i
    print(fact)

    return
#factorial(int(input()))

#2 second method  write a function for thr factorial of the number

def factorial(n):
   if n==0 or n==1:
       return 1
   else:
       fact=n*factorial(n-1)
       return fact

n=int(input("enter a number"))
print("factorial of",n,"is",factorial(n))

#3 write a function to the fibonacci series of the number
def fibnocci(n):
   if n<=1:
       return 1
   else:
       fib=fibnocci(n-1)+fibnocci(n-2)
       return fib
n=int(input("enter the number for fib series"))
print("fib series of",n,"is",fibnocci(n))
n=int(input("enter the number for fib series"))
print("fib series of",n,"is",fibnocci(n))