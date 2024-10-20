import os
import time


x = None
y = None

def add_numbers(a, b):
    return a + b 


while not isinstance(x, int) or not isinstance(y, int):
    try:
        print("x:")
        x = int(input())
        print("Y:")
        y = int(input())
    except ValueError:
        print("must be an integer")
   
    
# print(isinstance(x, int))
# print(isinstance(y, int))


print(add_numbers(x,y))

