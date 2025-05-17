# import math
# x = 16
# print(math.sqrt(x))

# from math import *
# print(sqrt(x))
# print(pi)

class_A = int(input("Enter the number of class A tickets sold: "))
class_B = int(input("Enter the number of class B tickets sold: "))
class_C = int(input("Enter the number of class C tickets sold: "))
total_sales = class_A * 1000 + class_B * 700 + class_C * 500
print("Total Sales: ", total_sales)