import pandas as pd

# Take in two values from a user (both in pounds) then convert those values to kilograms.

p = int(input("Enter your first weight value in pounds: "))

q = int(input("Enter your second weight value in pounds: "))


# The values are in pounds and we want to convert them to kilograms
# 1 pound = 0.4536 kilograms
# k is the constant = 0.4536
# To convert the inputs

pk = p * 0.4536
print("This is your first value in Kilograms: ", pk)

qk = q * 0.4536
print("This is your second value in Kilograms: ", qk)

# Perform the sum of the values.
K = pk + qk
print("The sum of the values is: ", K)

# Perform the average of the values.
# the average is usually the sum of the values provided divided by the number
# of values provided
# the number of values here is 2

print("The average of the values is: ", K/2)

# Find the difference between both values.
# since we want a positive difference

D1 = pk - qk
if D1 > 0:
 print("The difference between the values is: ", D1)
else:
 print("sorry, negative response")

D2 = qk - pk
if D2 > 0:
 print("The difference between the values is: ", D2)
else:
 print("sorry, negative response")

# Find the quotient when one value is divided by the other.
 print("The quotient is: ", pk / qk)

 print("The quotient is: ", qk / pk)

# Determine and print out whether any of the numbers are even or odd.
# an even number is a number that has no remainders when divided by 2
# an odd number number is a number that has a remainder when divided by 2

if (pk % 2) == 0:
  print("The first value is an even number")
else:
  print("The first value is an odd number")

if (qk % 2) == 0:
  print("The second value is an even number")
else:
  print("The second value is an odd number")
