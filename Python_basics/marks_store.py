# 📘 Student Marks Dictionary Program

## 📌 Description
# This Python program takes marks of three subjects from the user:


# The marks are stored inside a Python dictionary using the `update()` method and then printed as output.





# Creating an empty dictionary to store subject marks
dict1 = {}

# Taking Physics marks input from the user
x = input("phy's marks: ")

# Adding Physics marks into dictionary
# "phy" is the key and x is the value
dict1.update({"phy": x})

# Taking Chemistry marks input from the user
y = input("chem mark:")

# Adding Chemistry marks into dictionary
dict1.update({"chem": y})

# Taking Mathematics marks input from the user
z = input("maths mark: ")

# Adding Mathematics marks into dictionary
dict1.update({"maths": z})

# Printing the final dictionary containing all subject marks
print(dict1)


