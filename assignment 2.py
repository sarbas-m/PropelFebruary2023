#Assignment :2
#1 write a program to find the factorial of user input number.
#2 Given an integer n,print all integer less than or equal to n
#3 Given an integer ,print the sum of all even integer less than or equal to n
#4 Given n ,print the sum of all integers less than or equal to n which are divisible by 3 or 5

#Answers
"""
#1write a program to find the factorial of user input number.
n=int(input("enter a number"))
factorial=1
if n==0:
    print(1)
else:
    for i in range(1,n+1):
       factorial=factorial*i
    print(factorial)



#2 Given an integer n,print all integer less than or equal to n
n=int(input("enter a number"))
i=0
while i<=n:
    print(i,end=" ")
    i+=1

#3 Given an integer ,print the sum of all even integer less than or equal to n
n=int(input("enter a number"))
sum=0
for i in range(2,n+1,2):
    sum=sum+i
print(sum,end=" ")

#4 Given n ,print the sum of all integers less than or equal to n which are divisible by 3 or 5
n=int(input("enter a number"))
sum=0
for i in range(1,n+1):
    if ((i%3==0)|(i%5==0)):
        sum=sum+i
print(sum)
"""
