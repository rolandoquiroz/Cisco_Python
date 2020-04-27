"""
Adding elements to a list: append() and insert()

A new element may be glued to the end of the existing list:
list.append(value)

Such an operation is performed by a method named append(). It takes its argument's value and puts it at the end of the list which owns the method.

The list's length then increases by one.

The insert() method is a bit smarter - it can add a new element at any place in the list, not only at the end.
list.insert(location, value)

It takes two arguments:

    the first shows the required location of the element to be inserted; note: all the existing elements that occupy locations to the right of the new element (including the one at the indicated position) are shifted to the right, in order to make space for the new element;
    the second is the element to be inserted.

"""

myList = [] # creating an empty list

for i in range(5):
    myList.append(i + 1)

print(myList)

otherList = [] # creating an empty list

for i in range(5):
    otherList.insert(0, i + 1)

print(otherList)