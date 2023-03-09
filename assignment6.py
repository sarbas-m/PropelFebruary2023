"""
#Assignment 6

1.write a function that takes two lists nad returns a new list with elements that are common to
both the lists. The new list should not have any duplicates and input lists may be of different lengths.

a=[1,2,45,52,45,66,79,89,2,"c"]
b=[40,2,66,37,89,"c"]
c=[]

def unionList():
    for i in a:
        if i in b:
            c.append(i)
    x=set(c) #to remove duplicate coverts to set
    print(list(x))

unionList()
#input method
a=[]
b=input("enter the elements for list1:").split(",")
c=input("enter the elements for list2:").split(",")
print("list1 is",b)
print("list2 is",c)

for i in b:
    if i in c:
        a.append(i)
#print(a)
x=set(a)
print("common list of both is",list(x))

2.	The multiplicative persistance of a positive integer is the number of steps required
 to get a one digit number when separating the digits and multiplying them.
  for example : the multiplicative persistance of 39 is 3 because
39-->27-->-->14-->4

number=input("enter a number: ")
a=[]
while len(number)>1:
     n=1
     for i in number:
        n=n*int(i)
     a.append(n)
     number = str(n)
print("sequnce is",a)
print("multilplicative persistance is",len(a))
"""


"""
3.	given an positive integerr n, if you apply the following rukes iteratively, you will eventually
 get a 1. it is called collatz sequence
n---> n/2 (if n is even)
n---> 3*n+1 (if n is odd)
for example 13->40->20->10->5->16->8->4->2->1
write a function to genrate the collatz sequence. now find the starting number less than 1 million which will produce the longest chain


n=int(input("enter the number:"))
def collatz(n):

 if n%2==0:
    print(n//2,end=",")
    return n//2
 else:
    print(3*n+1,end=",")
    return 3*n+1
while n!=1:
    n=collatz(n)
"""