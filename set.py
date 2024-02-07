# What is a set in Python?
# A set is an unordered collection of unique elements, created using curly braces {} or the set() constructor.
#set->mutable 

# How do you add elements to a set?
# Elements can be added using add() method or by using the update() method to add multiple elements.

# What is the main characteristic of a set?
# Sets contain unique elements, so they automatically remove duplicates.
# Supports set operations like union, intersection and difference.

# 1. Using Set
# my_list = [1, 2, 3, 4, 2, 3]
# unique_set = set(my_list)
# print(unique_set)

# 2. Check if Two Sets are Disjoint:->checks is set1 and and set2 are different?
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# # Using isdisjoint()
# disjoint = set1.isdisjoint(set2)->gives true or false
# print(disjoint)

# 3. Find the Union of Two Sets:
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# # Using Union Operator |
# union_set = set1 | set2
# print(union_set)


# 4. Find the Intersection of Two Sets
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# # Using Intersection Operator &
# intersection_set = set1 & set2
# print(intersection_set)

# 5. Find the Difference Between Two Sets:
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# # Using Difference Operator -
# difference_set1 = set1 - set2 #->returns the elements in set1 by removing elements in set2
# print(difference_set1)
# difference_set2 = set2 - set1 #->returns the elements in set2 by removing elements in set1
# print(difference_set2)

# 6. Check if a Set is a Subset of Another Set:
# set1 = {1, 2, 3, 4, 5}
# set2 = {2, 4}

# # Using issubset()
# subset = set2.issubset(set1) #gives true or false
# print(subset)

# 7.Add an element to set
# my_set = {1, 2, 3}

# # Using add()
# my_set.add(4)
# print(my_set)

# 8. REmove an element from set
# my_set = {1, 2, 3}

# # Using remove()
# my_set.remove(2)->removes the element 2 from set
# print(my_set)

# 9. Check if a Set is Empty:
# my_set = set()

# # Using not
# if not my_set:
#     print("Set is empty")