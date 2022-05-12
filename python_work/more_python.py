# print("not the bees")





# print (int(5.4))
# print (int("54"))  

# print (float(54))

# print (type(str(54)))
# print (type(str(5.4)))
# ------------------------------------------------

# Truthy and falsy
# name=input()
# if name:
#     print (f"Hello {name}")
# else:
#     print("you did not provide name")

#not oparator -------------------------------  

# print(not True)
# print(not False)

# bool = False 
# if bool != True:
#     print(False)
# else:
#     print(True)

# #----------------

# bool = False 
# if not bool != True:
#     print(False)
# else:
#     print(True)
#----------------------

# 5
#------------------------------


# def add_up():
#     num1 = input ("enter 1")
#     num2 = input ("enter 2")

#     try:
#         print(f"{num1}  +   {num2} is {int(num1) + int(num2)}")

#     except:
#         print("Error!")
#         print("*******")
#         add_up()

# add_up()

#-----------------
#scope global/local

# light = False 

# def light_switch():
#     global light
#     if light:
#         print("whao! it is bright")
#         light = False
#     else:
#         print("Who turned out the light?")
#         light = True

# light_switch()
# light_switch()

#-------------- 
#cash machine global veriant
# balance = 100

# def cash_withdraw(amount):
#     global balance
#     print(f"your balance is {balance}")
#     print(f"you are with drawing {amount}")
#     balance -=amount
#     print(f"your new balance is {balance}")

# cash_withdraw(20)
# cash_withdraw(20)
# cash_withdraw(20)

#--------------- 
# lists and tuples

# list1 = [
#     1,2,3]


# tuple1 = (
#     1,2,3
# )

# list_or_lists[
#     [1,2,3],
#     [4,5,6]
# ]

# print(list_pf_list)


# even_nums = [2,4,6,8,10]

# odd_nums = (1,3,5,7,9)

# even_nums.append(12)
# even_nums.insert(0, 0)

# for i in even_nums:
#     print(i)

# odd_nums.remove(1)
# odd_nums.pop(1)

# list_of_fruit =[
#     "apples",
#     "bananas",
#     "cherries",
#     "pineapple",
#     "jack-fruit"
# ]

# print(list_of_fruit[1:4])

# nums = [0,1,2,3,4,5,6,7,8,9,10]

# print (nums[0:11:4])


#---------------------------------------

# mun = 0

# while num <10:
#     print(num)
#     num += 1

