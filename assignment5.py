"""
#Assignmnet 5

1.Write a function named sort_odd_even() that will  sort a list of numbers with the odd numbers coming
first and the even numbers coming second. You can use the list.sort function.

b=[]
even=[]
odd=[]
def sort_odd_even():
       total_input=int(input("enter the total input"))
       for i in range(total_input):
           a=int(input("enter the number"))
           b.append(a)
       for i in b:
               if i%2==0:
                   even.append(i)
                   even.sort()
               else:
                   odd.append(i)
                   odd.sort()
       print(odd+even)
sort_odd_even()

2. By using list comprehension, write a program to print the list after removing the
 value 24 in [12,24,35,24,88,120,155].

l=[12,24,35,24,88,120,155]
newList=[i for i in l if i!=24]
print(newList)


3. Use a list comprehension to square each odd number in a list. The list is input by a sequence of
comma-separated numbers.

a=[]
odd=[]
s=[]
for i in range(int(input("enter the total input number:"))):
    n=int(input("enter the number:"))
    a.append(n)
for i in a:
        if i%2!=0:
            odd.append(i)
print(odd)
for i in odd:
    sq=i**2
    s.append(sq)

print(s)

numbers=input("enter the numbers seperated by commas:")
x=numbers.split(",")
#or
l=[2,3,4,5,6,7,10,22,2,1,43,45,40]
l1=[i**2 for i in l if i%2==1]
print(l1)

#or

a=input("enter the elements in the list seperated by comma:")
newList=[int(x)**2 for x in a.split(",") if int(x)%2!=0]
print(newList)

4.Using list comprehension, return the number of even integers in the given array.

a=[1,2,8,5,46,45,21,2]
b=[i for i in a if i%2==0]
print(b)

5.Use filter() to eliminate all words that are shorter than 4 letters from a list of words.


def remove_words(list1):
    result=list(filter(lambda s :len(s)>3,list1))
    print(result)
list1=['hello','world','iam']
remove_words(list1)
#or
l=[x for x in input("enter the words").split(" ")]
def shorter(y):
    if len(y)>3: #y for iteration through list
        return True
    return False
x=filter(shorter,l)
print(list(x))



6.Write a list comprehension statement to convert a list of Fahrenheit temperatures to Celsius

x=[100,32,45,18,40]
a=[(i-32)*5/9 for i in x]
print(a)


7.Use map and a lambda function to convert a list of Fahrenheit temperatures to a list of Celsius temperatures

l=[32,45,100,89,47]
f=lambda t:(t-32)*5/9
c=list(map(lambda t:(t-32)*5/9,l))
print(c)


8. Input two lists and convert the two list to dictionary.

a=[]
b=[]
c=int(input("enter the total input elements:"))
for i in range(c):
    d=input("input for list 1: ")
    a.append(d)
for i in range(c):
    e=input("input for list 2 : ")
    b.append(e)
print(a)
print(b)
x=dict(zip(a,b))
print(x)
#or
y={k:v for k,v in zip(a,b)}
print(y)




9. Make a two-player Rock-Paper-Scissors game. One of the players is the computer. 10 chances.
Print out the winner and points earned by both players.
Remember the rules:
Rock beats scissors Scissors beats paper Paper beats rock

import random
import re
player=[]
computer=[]
n=1
while n<=5:
 a=["rock","paper","scissor"]
 player_choice=input('''enter the choice:
                1.rock
                2.paper
                3.scissor
                =>''')
 computer_choice=random.choice(a)
 print(player_choice)
 print(computer_choice)
 if player_choice==computer_choice:
    print(f"both players seleceted {player_choice},it is tie")
    player.append("tie")
    computer.append("tie")
 elif player_choice=="rock":
    if computer_choice=="paper":
        print("paper beats rock")
        computer.append("win")
    else:
        print("rock beats scissor")
        player.append("win")
 elif player_choice=="paper":
    if computer_choice=="rock":
        print("paper beats rock")
        player.append("win")
    else:
        print("scissor beats paper")
        computer.append("win")
 elif player_choice=="scissor":
    if computer_choice=="rock":
        print("rock beats scissor")
        computer.append("win")
    else:
        print("scissor beats paper")
        player.append("win")
 n+=1
print("player score:",player)
print("computer score:",computer)
if len(player)==len(computer):
    print("match tie")
elif len(player)>len(computer):
    print("player wins")
else:
    print("computer wins")



10. Write a program which accepts a sequence of comma-separated numbers from console and generate
 a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

a=input("enter the numbers seperated by commas: ")
b=a.split(",")
print(b)
print(type(b))
c=tuple(b)
print(tuple(b))
print(type(c))

11. Write a program that accepts a comma separated sequence of words as input and prints the words
 in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world


a=input("enter the words seperated by commas:" )
b=a.split(",")
b.sort()
print(b)
for i in b:
    print(i,end=",")


12. Write a program which accepts a sequence of comma separated 4 digit binary numbers as its
 input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed
  in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010


a=str(input("enter the numbers: "))
b=a.split(",")
for i in b:
    if int(i,2)%5===0:
        print(i,end",")
#or

a=input("enter the 4 digit binary numbers with,seperated:")
value=[]
items=[x for x in a.split(",")]
for p in items:
    decimel=int(p,2)
    if not decimel%5:
        value.append(p)
print(",".join(value))
"""