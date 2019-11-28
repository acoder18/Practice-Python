#This script it to generate two random numbers and add them
#and compare respose from user to see if he is right

# import random
# for i in range(1,100):
#     num1 = random.randint(1, 100)
#     num2 = random.randint(1, 100)
#     print str(num1) + str num2

import random

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
    
print ("What is " + str(num1) + " + " + str(num2))

answer = num1 + num2

yourAnswer = int(input())

while True:
    if answer != yourAnswer:
        # print ("Nope")
        continue
    else:
        print  ("Awesome")
