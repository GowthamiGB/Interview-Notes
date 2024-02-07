# What is a dictionary in Python?
# A dictionary is an unordered collection of key-value pairs, created using curly braces {}.
# Each key is separated by its value using :, and other keys are separated by (,)comma. 

# How do you access values in a dictionary?
# Values in a dictionary are accessed using their associated keys. Example: my_dict['key']->mutable.

# How do you add or update elements in a dictionary?
# Elements can be added or updated using assignment. Example: my_dict['new_key'] = 'value'.

# What happens if you try to access a key that doesn't exist in a dictionary?
# It raises a KeyError. To avoid this, you can use get() method or check for existence using "in" operator.

# 1. Create a dictionary with keys and values
# my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
# print(my_dict)

# 2. Access the value associated with the 'age' key
# my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
# age = my_dict['age']
# print(age)

# 3. Add a new key-value pair to the dictionary
# my_dict = {'name': 'John', 'age': 25}
# my_dict['city'] = 'New York'
# print(my_dict)

# 4. Modifying an existing element in dictionary
# my_dict = {'name': 'John', 'age': 25}
# my_dict['age'] = 50
# print(my_dict)

# 5. Check if the 'city' key exists in the dictionary -> in,not in
# my_dict = {'name': 'John', 'age': 25}
# key_exists = 'city' not_in my_dict
# print(key_exists) -> gives true or false

# 6. Like LIST COMPREHENSION, dictionary can be used 
# squares = {x : x ** 2 for x in range(5)}
# print(squares)

# 7. For deleting -> del
# my_dict = {'name': 'John', 'age': 25}
# del my_dict['name']
# print(my_dict)

# METHODS
# 8. Length -> len()
# my_dict = {'name': 'John', 'age': 25}
# print(len(my_dict))

# 9. Remove the 'age' key and its associated value -> pop()
# my_dict = {'name': 'John', 'age': 25}
# my_dict.pop('age')
# print(my_dict)

# 10. Iterate through the key-value pairs in the dictionary 
# .items ->iterates through for loop and gives "tuple" output
# my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
# for i in my_dict.items():
#     print(i)

# 11. Get values of the dictionary->.values()
# my_dict = {'name': 'John', 'age': 25}
# print(my_dict.values())

# 12. Merge two dictionaries -> merged_dict = {**dict1, **dict2}
# dict1 = {'name': 'John', 'age': 25}
# dict2 = {'city': 'New York', 'country': 'USA'}
# merged_dict = {**dict1, **dict2}
# print(merged_dict)

# 13. get()->will give value if present. If not then gives None. But will not give KeyERROR. 
# my_dict = {'name': 'John', 'age': 25}
# print(my_dict.get('city'))

# my_dict = {'name': 'John', 'age': 25}
# print(my_dict['city']) -> this gives KeyError

# 14. A shallow copy creates a new object but does not create new objects for nested elements.
#  It copies the references to the nested objects.Changes made to nested objects inside the copied 
# structure will be reflected in both the original and the shallow copy.
# In Python, you can use the copy() method for dictionaries and lists to create a shallow copy.

# import copy
# original_list = [1, [2, 3], [4, 5]]
# shallow_copy_list = copy.copy(original_list)
# # Modify a nested list in the shallow copy
# shallow_copy_list[1][0] = 99
# print("Original List:", original_list)
# print("Shallow Copy List:", shallow_copy_list)

# OUTPUT:
# Original List: [1, [99, 3], [4, 5]]
# Shallow Copy List: [1, [99, 3], [4, 5]]

# A deep copy creates a completely independent copy of the original object along with all its nested objects.
# Changes made to the nested objects inside the copied structure do not affect the original object, and vice versa.
# In Python, you can use the copy module's deepcopy() function for dictionaries and lists to create a deep copy.

# import copy
# original_list = [1, [2, 3], [4, 5]]
# deep_copy_list = copy.deepcopy(original_list)
# # Modify a nested list in the deep copy
# deep_copy_list[1][0] = 99
# print("Original List:", original_list)
# print("Deep Copy List:", deep_copy_list)

# OUTPUT:
# Original List: [1, [2, 3], [4, 5]]
# Deep Copy List: [1, [99, 3], [4, 5]]

