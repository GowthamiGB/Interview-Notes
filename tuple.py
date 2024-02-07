# A tuple is a collection of ordered and immutable elements,allows duplicates, created using parentheses ().
# Tuples are used to group together related pieces of data.
# Tuples can be used to represent fixed sets of values, such as coordinates, configurations, or data records.
# Elements in a tuple are accessed by their index, similar to lists, using square brackets [].
# Heterogeneous Elements:Tuples can store elements of different data types in a single tuple.
# Supports Nesting: Tuples can be nested within other tuples, allowing the creation of complex data structures.
# eg: tuple inside a tuple:toppers=(('gow','be'),('jhe','bams'))
# Hashable:Tuples are hashable and can be used as keys in dictionaries, making them suitable
# for certain use cases where mutability is not desired.
# Multiple Assignment:a, b, c, d = my_tuple 


# When writing single element put comma after element as it treats it as tuple. else it consideres as integer.
# tup=(10, )
# print(type(tup))

# Normal comma separated values are also treated as tuples->10,20

# divmod()->quo,rem=divmod(100,3)-this returns the quotient and remainder

# Tuple allows the variables on lhs to be assigned with tuples on rhs
# eg:(v1,v2,v3)=(1,2,3)
# print(v1,v2,v3)

# Tuple can have expressions in it when assigning
# eg:(v1,v2)=(2*2,3+1+1)
# print(v1,v2)


# tup=(10,20)
# print(tup.index(20))->gives the index value

# tup=(10,20,10)
# print(tup.count(10))->gives the occurance count

# swap values using tuple
# v1=10
# v2=20
# print(v1)
# print(v2)
# (v1,v2)=(v2,v1)
# print("after swap of v1:",v1)
# print("after swap of v2:",v2 )


# 1. Question: Concatenate two tuples
# tuple1 = (1, 2, 3)
# tuple2 = ('a', 'b', 'c')
# concatenated_tuple = tuple1 + tuple2
# print(concatenated_tuple)

# 2. Find the Maximum Number in a List- all same like list but initialization is ()
# tuple_numbers = (1, 2, 3, 4, 5)
# max_ele = tuple_numbers[0]
# for i in tuple_numbers:
#     if i > max_ele:
#         max_ele = i
# print(max_ele)

# 3.# Find the minimum and maximum elements in the given tuple without using min() and max()
# numbers_tuple = (5, 2, 8, 1, 7)
# min_element = sorted(numbers_tuple)[0]
# max_element = sorted(numbers_tuple)[-1]
# print("Minimum:", min_element)
# print("Maximum:", max_element)

# 4. # Check if 'apple' exists in the given tuple without using 'in'
# fruits_tuple = ('apple', 'banana', 'cherry')
# element_exists = any(item == 'apple' for item in fruits_tuple)
# print(element_exists) ->gives true if atleast one occurance is present  or false-any

# fruits_tuple = ('apple', 'banana', 'cherry')
# item='apple'
# if item in fruits_tuple:
#     print('present')
# else:
#     print('item not present')

# 5. Find the length of the given tuple without using len()
# my_tuple = ('apple', 'banana', 'cherry')
# length_of_tuple = sum(1 for i in my_tuple)
# print(length_of_tuple)

# my_tuple = ('apple', 'banana', 'cherry')
# length_of_tuple = len(my_tuple)
# print(length_of_tuple)

# fruits_tuple = ('apple', 'banana', 'cherry')
# len=0
# for i in fruits_tuple:
#     len+=1
# print(len)


#  6. Reverse a Tuple without built-in
# tuple_numbers = (1, 2, 3, 4)
# reverse_tuple = tuple_numbers[::-1]
# print(reverse_tuple)

# APPEND not there in tuple
# 7. Remove Duplicates from a Tuple without built-in
# tuple_numbers = (1, 2, 3, 4, 2, 3)
# unique = tuple(i for i in tuple_numbers if tuple_numbers.count(i) == 1)
# print(unique)


# APPEND not there in tuple-> but can use list then make it as tuple
# tuple_numbers = (1, 2, 3, 4, 2, 3)
# unique=[]
# for i in tuple_numbers:
#     if i not in unique:
#         unique.append(i)
# print(tuple(unique))

