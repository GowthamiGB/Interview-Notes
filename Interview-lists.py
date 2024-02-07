# List-A list is a collection of items, 
# ordered and mutable, allowing duplicate elements. It's created using square brackets [].
# Key-element->lists can have elements belonging to different datatypes and can over-write the elements

# Creation: my_list = [1, 2, 3, 'a', 'b']
# Access: first_element = my_list[0]  # Access the first element
# Modification: my_list[2] = 'new_value'  # Modify the third element
# Append: my_list.append('new_element')  # Add an element to the end
# Insert: my_list.insert(2, 'inserted')  # Insert an element at a specific index
# Remove: my_list.remove('a')  # Remove the first occurrence of 'a'
# Delete: del my_list[1]  # Delete the second element
# Length: length = len(my_list)  # Get the length of the list

# l=[1,2,3,4,5,6,7]

# print(len(l))->ans=7
# print(5 in l)->True, print(5 not in l)->False
# print(max(l))->7
# print(min(l))->1
# print(sum(l))->gives total
# print(sorted(l))->gives sorted value of list
# l=list('h','e','l','l','o')->print(l)->gives ['h','e','l','l',o]

# Methods->
# extend() adds multiple elements (from an iterable) to the end of a list.
# print(l.append(100))->l=[1,2,3,4,5,6,7,100] 
# print(l.del[1]) ->elememt in 1st index is deleted->l=[1,3,4,5,6,7]
# print(l.count(3))->number of times an element(3) occurances->here once
# print(l.index(3))->returns the lowest index of the element 3->here 2
# print(l.insert(2,100))->inserts 100 at index 2
# print(l.pop())->removes the last element->can specify the index also .pop(2)
# print(l.remove(3))->removes from the lowest index of element 3
# print(l.reverse())->reverses the list
# print(l.sort())->sorts the list 

# LIST-COMPREHENSION
# It allows you to create a new list by specifying the elements you want
# to include and the conditions they must meet
# eg: squares = [x ** 2 for x in range(5)]
# print(squares) ->[0, 1, 4, 9, 16]

# ENUMERATE->input is list and gives output as tuple 
# this helps in replacing the values.when index value is divided by 2 then replace by 'xx'.
# for index,i in enumerate(l):
# print(i,'is at index:',index)-> gives value with index in the form of tuple

#  ALL ARE SAME FOR TUPLE ALSO BUT INITIALIZATION USING ()
# 1.Find the Maximum Number in a List
# Built-in
# list=[1,2,3,4,5]
# print(max(list))


# Linear Search
# list=[1,2,3,4,5]
# max_ele=list[0]
# for i in list:
#     if i>max_ele:
#         max_ele=i
# print(max_ele)

# 2.Calculate the Sum of Numbers in a List:
#Built-in
# list=[1,3,5,7,9]
# print(sum(list))

#no-built-in
# list=[1,3,5,7,9]
# sum_ele=0
# for i in list:
#     sum_ele+=i
# print(sum_ele)

# 3.Remove Duplicates from a List:
# built-in
# list=[1,2,3,4,2,3]
# print(set(list))

# no built-in
# list=[1,2,3,4,2,3]
# unique=[]
# for i in list:
#     if i not in unique:
#         unique.append(i)
# print(unique)

# 4. Reverse a List:
# built-in-slicing
# list=[1,2,3,4]
# print(list[::-1])

# no built-in
# list=[1,2,3,4]
# reverse_list=[]
# for i in range(len(list)-1,-1,-1):
#     reverse_list.append(list[i])
# print(reverse_list)




# 5. Check if List is Palindrome:
# List-slicing
# def is_palindrome(list):
#     return list==list[::-1]
# list1=[1,2,2,1]
# list2=[1,2,3,4]

# print("Is palindrome",is_palindrome(list1))
# print("Is palindrome",is_palindrome(list2))

# no-built-in
# list=[1,2,2,1]
# is_palindrome=True
# for i in range(len(list)):
#     if list[i]!=list[len(list)-i-1]:
#         is_palindrome=False
#         break
# if is_palindrome:
#     print("Palindrome")
# else:
#     print('Not a palindrome')


# 6. Count Occurrences of an Element in a List:
# in-built
# def occurance(list,element):
#     return(list.count(element))
# list=[1,2,2,2,3]
# element=2
# print(occurance(list,element))

# no-in_built-for 1 element occurance
# list=[1,2,2,2,2,3]
# occurance=[]
# count=1
# for i in list:
#     if i not in occurance:
#         occurance.append(i)
#     else:
#         count+=1
# print(count)

# if element is specified
# list=[1,2,2,2,2,3,3,4,4,4,4,4,4]
# ele=4
# count=0
# for i in list:
#     if i==ele:
#         count+=1
# print(count)
