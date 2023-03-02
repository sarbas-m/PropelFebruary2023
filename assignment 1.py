#Assignmnet 1
#1 write a program to check whether the input number is odd or even
#2 write a pgm to to check whether the input number is prime number
#3 write a pgm to check whether a person is eligible for voting or not
#4 write a pgm to check whether a number is divisible by 7 or 8
#5 write a pgm to calculate the electricity bill(accept from user)
  #unit                     Price
  #first 100 units          no charge
  #next 100 units           Rs 5 Charge
  #After 200 units          Rs 10 per unit
  #(for exmple if input unit is 350 then total bill amount is Rs2000)
"""
#Answers
#1write a program to check whether the input number is odd or even
number=int(input("Enter a number"))
if number%2==0:
    print("it is even number")
else:
    print("it is odd")

#2write a pgm to to check whether the input number is prime number

number=int(input("Enter a number"))
if number==0:
    print("it is not prime number")
elif number==2:
    print("it is prime number")
elif number%2==0:
    print("it is not prime number")
else: number%2!=0
print("it is not prime")

#3write a pgm to check whether a person is eligible for voting or not
age=int(input("Enter your age"))
if age==18:
    print("you are eligible for voting")
elif age>18:
    print("you are eligible for voting")
else:
    print("you are under 18,not eligible for voting")

#4write a pgm to check whether a number is divisible by 7 or 8
number=int(input("enter the number"))
if number%7==0:
    print("number is divisible by 7")
elif number%8==0:
    print("number is divisible by 8 ")
else:
    print("not divisible")


#5write a pgm to calculate the electricity bill(accept from user)

unit=int(input("enter the unit"))
if unit<=100:
    bill=0
    print(bill)

else:
    if unit-100<=100:
        bill1=(unit-100)*5
        bill=bill1
        print(bill)
    else:
        bill1=100*5
        bill2=(unit-200)*10
        bill=bill1+bill2
        print(bill)
"""