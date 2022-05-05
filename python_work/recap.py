from asyncore import loop
from operator import index
import random
# #python notes recap lv 2
# #print works with a hashtag

# Print("this is my current file")

# # greeting = "Hello World"
# # print = "Hello world"


# # stings are for representing chartictors
# print ("Hello my name is dami")

# #This is a intiger (whole number)
# print (1234)

# #this is a floating point (decimel point)
# print (1234.5)

# #boolean - True and False
# print(True)
# print(False)

# #Len & 0 count 
# print(len("hello"))
# print ("hello [-1]")

# print(random.random())
# print(random.uniform(1,10))
# print(random.randint(1,10))

# import random
# from random import random, randint,uniform

# my_name = "dami"
# my_age = 26

# print(my_name)

# print("Hello my name is",my_name)
# print("Hello I am" + my_name)
# print("Hello my name is {} and I am {} years old".format(my_name,my_age)) #dot format
# print(f"Hello my name is {my_name} and I am {my_age} years old") # F strings

# math opperators
# print(1+2)
# print(2-1)
# print(2*3)
# print(3**3)
# print(15/3)
# print(15%3)

# balance = 100
# amount = 50

# print(balance-amount)
# balance = balance - amount
# balance -=amount

# print(balance)

# char_name = input("What is your name?   >    ")

# print(f"welcome, {char_name}")

#if statement
# music = "classical"

# if music =="classical":
#     print("oh no it's classical!")
# elif music == "pop":
#     print("turn it up")
# else:
#     print("yay")

#grater then or equil to: >=, greater then >, less then equils <=

# num1=10
# num2=20

# if num1 > num2:
#     print("number 1 is the bigger number")
# elif num1<num2:
#     print("number 2 is the bigger number")
# else:
#     print("number 1 and number 2 are the same")

# num = 21 
# if num%7==0 and num%3==0:
#     print("fizzbuzz")
# if num%3==0:
#     print("fizz")
# elif number%7==0:
#     print("buzz")
# else:
#     print (num)


# place = "Manchester"
# weather = "cloudy"

# if  place=="Manchester" and weather=="Cloudy":
#     print("of course")
# elsif  place=="Manchester" and weather=="sunny":


#Functions

# def light_switch():
#     print("who truned out the lights")

# light_switch()



#lists

# fav_films=[
#     "Jurassic Park",
#     "Lost World",
#     "The Matrix"
# ]

# # fav_films.append("Monster Hunter")

# #loops

# for i in fav_films:
#     print("Really good film") #dont need to always refrance index

# for i in range(10):
#     print(i)

# welcome = "Welcome to code nation"


#TASK 1
# result = "welcome to code nation"
# resul=len(result)

# print(result)
# def phrase_check ():
#     if result %2 == 0:
#         print(welcome,result,"Even Number!")
#     else:
#         print( result,"An odd number!")
# phrase_check ()

#TASK 2

alphabet =["a","b","c","d","e","f","g","h","i","j","k","l","m","o","P","q","r","s","t","u","v","w","x","y","z"
]

for i in alphabet:
    print (i)
rand_num = (int)(input("pick a number??"))


def rand_letter():
    rand_letter=input("pleas")