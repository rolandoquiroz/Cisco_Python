#!/usr/bin/python3
"""
Objectives

Familiarize the student with:

    using basic instructions related to lists;
    creating and modifying lists.

Scenario

There once was a hat. The hat contained no rabbit, but a list of five numbers: 1, 2, 3, 4, and 5.

Your task is to:

    write a line of code that prompts the user to replace the middle number in the list with an integer number entered by the user (step 1)
    write a line of code that removes the last element from the list (step 2)
    write a line of code that prints the length of the existing list (step 3.)
"""


hatList = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.
print("Current list: ", hatList)
print("Current list lenght: ",len(hatList))
# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
hatList[2] = input("Please enter a integer number to replace the middle number: ")
print("Current list: ", hatList)
print("Current list lenght: ",len(hatList))
# Step 2: write a line of code here that removes the last element from the list.
del(hatList[len(hatList) - 1])

# Step 3: write a line of code here that prints the length of the existing list.
print("Current list: ", hatList)
print("Current list lenght: ",len(hatList))