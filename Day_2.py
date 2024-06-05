# Data Types
# string

print("hello"[-4])

"123"

#  integer

print(123 + 334)

# 123_456_789 is the same as 123456789, "_" can replace ","
# Float

3.14159

# boolean

True
False
num_char = len(input("what is your name?"))
new_num_char = str(num_char)
print("your name has " + new_num_char + " charters.")
two_digit_number = input("type a two digit number: ")
first_num = two_digit_number[0]
second_num = two_digit_number[1]
result = int(first_num) + int(second_num)
print(result)
3 + 5
7 - 3
3 * 2
5 / 6

print(5 ** 2)  # 5 raised to the power of 2
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
result = float(weight) / float(height) ** 2
print(round(result))

# print(round(2.66666666666, 2)) #round to 2 decimal places
# print(8//3) #the output is an integer

# -=
# +=
# /=

bat

score = 0
height = 1.8
isWinning = True
# f-string
print(f"your score is {score}")
age = input("What is your current age? ")
days = (90 - int(age)) * 365
weeks = (90 - int(age)) * 52
months = (90 - int(age)) * 12

print(f"You have {days} days, {weeks}, and {months} months left.")
print("Welcome to the tip calculator.")
bill = float(input("what was the total bill? $"))
tip = int(input("what percentage tip would you like to give? 10, 12, or 15? "))
person = int(input("How many people to split the bill?"))
# total= (int(bill)/int(person))*(float(tip)/100)
# print(f"Each person should pay: ${round(total,2)}")
tip_as_percent = tip / 100
precent_of_bill = bill * tip_as_percent
total_bill = bill + precent_of_bill
payment = total_bill / person
final_amount = "{:.2f}".format(payment)
print(f"Each person should pay: ${final_amount}")
