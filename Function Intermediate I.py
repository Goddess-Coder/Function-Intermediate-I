#With this concept of default parameters in mind, the goal of this assignment is to write a single function, randInt() that takes up to 2 arguments.
# If no arguments are provided, the function should return a random integer between 0 and 100.
# If only a max number is provided, the function should return a random integer between 0 and the max number.
# If only a min number is provided, the function should return a random integer between the min number and 100
# If both a min and max number are provided, the function should return a random integer between those 2 values.

# Floating number between 0 and 100
import random
def randInt(min= 0 , max=100):
    print(random.randint(0, 100))
print(randInt()) 

#Floating number between 0 and max
import random
def randInt(max=1000):
    print(random.randint(0, max))
print(randInt()) 

#Floating number between min and 100
import random
def randInt(min=25):
    print(random.randint(min, 100))
print(randInt()) 

#Floating number between min and max
import random
def randInt(min=100, max=200):
    print(random.randint(min, max))
print(randInt())
