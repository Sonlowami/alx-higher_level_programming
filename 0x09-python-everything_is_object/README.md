# 0x09. Python - Everything is object

In Python, there are some common behaviors and functionalities that all things share.
These are things like having a string representation, storing a map of it's attributes and
there values, and the ability to remove or add an attribute to itself.

For Python to guarantee all these common features, everything must be an object. In human terms,
this means everything in Python have a common ancestor.
Everything being an object have specific implications, that might not be evident at once. Multiple
variables can refer to the same object. When this happens, the object is said to be aliased.
But two variables can have the same value, and not be pointing to the same object.

## So, how do you know if two variables point to the same variable or not?

You can use the ```is``` operator to check if variables point to the same object or not. The operator
returns a boolean.

## About this repository

This repository contain solutions to programming challenges by Holberton, that circles around identifying
whether variables refer to the same object or not.
