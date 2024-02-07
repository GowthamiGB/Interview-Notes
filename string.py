# A string is a sequence of one or more characters, letter, digit, space in Python.(ordered)
# strings are "immutable", which means that once a string is created, its value cannot be changed. However, 
# you can perform various operations on strings, 
# such as concatenation, slicing, and formatting, to manipulate and work with the data they represent.


# 1. Creating Strings:
# You can create strings using single quotes (') or double quotes (").
#  Triple quotes (''' or """) are used for multiline strings.
# single_quoted_string = 'Hello, World!'
# double_quoted_string = "Python Programming"
# multiline_string = '''This is a
# multiline
# string.'''

# 2. Accessing Characters:
# You can access individual characters in a string using indexing. Python uses zero-based indexing.

# my_string = "Python"
# first_char = my_string[0]  # 'P'
# third_char = my_string[2]  # 't'


# 3. String Operations:
# Strings support various operations, including concatenation(+) and repetition or multiplication(*).

# str1 = "Hello"
# str2 = "World"
# concatenated_str = str1 + " " + str2  # 'Hello World'
# repeated_str = str1 * 3  # 'HelloHelloHello'


# 4. String Methods:
# Python provides a variety of built-in methods for working with strings, such as 
# len(), upper(), lower(), find(), replace(), and more.

# my_string = "Python Programming"
# length = len(my_string)  # 18
# upper_case = my_string.upper()  # 'PYTHON PROGRAMMING'
# lower_case = my_string.lower()  # 'python programming'
# index_of_o = my_string.find('o')  # 4
# replaced_string = my_string.replace('Programming', 'Language')  # 'Python Language'


# 5. String Formatting: f-> for formatting
# String formatting allows you to create dynamic strings by inserting values into placeholders.

# name = "Alice"
# age = 30
# formatted_string = f"Hello, my name is {name} and I am {age} years old."


# 6. Escape Characters:-> inorder to overcome real meaning. ('\')
# Escape characters are used to represent special characters in strings.

# escaped_string = "This is a line\nThis is a new line"
# output:This is a line
# This is a new line

# escaped_string = "This is a line\\nThis is a new line"
# print(escaped_string)
# output: This is a line\nThis is a new line

# 7. Raw Strings:(r or R)->want to specify exactly as specified
# Raw strings treat backslashes as literal characters and are useful when working with regular expressions or file paths.

# raw_string = r"C:\Users\Username\Documents"


#  some of the string methods
# str.Capitalize()->first letter will be capital
# str.count(string,beg,end)->eg: str=he ->msg.count(str,0,len(msg))->number of time the word is repeated
# str.endswith(suffix,beg,ending)-> gives true or false
# str.startswith(prefix,beg,end)->gives true or false
# str.find(str,beg,end)->left to right->gives index->1st occurance index
# str.rfind(str,beg,end)->right to left->gives index->1st occurance index
# str.isalnum()->true or false-> alpha and number if present
# isalpha(),isdigit()->for both true if atleast one occurance is present.
# islower(),isspace(),isuper()->gives true or false
# str.lstrip()->removes white spaces from left
# str.rstrip()->removes white spaces from right
# str.strip()->removes white spaces from both left and right
# str.split('delimiter)->delimiter can be space,\t ,','.->if not specified then on white spaces

# list=['abc','def']
# print('-'.join(list)) #join using delimiter
# output: abc-def

# string slicing
# string = 'PYTHON'
# print(string[0:2]) #PY

# Extra
# 1. Factorial Program:
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n* factorial(n-1)
# n=5
# print("factorial is:",factorial(n))

# 2.Palindrome Program:
# def is_palindrome(string):
#     return string==string[::-1]
# string='radar'
# if is_palindrome(string):
#     print("palindrome")
# else:
#     print("Not a palindrome")

# 3.Fibonacci Program:

# Fibonacci(0) = 0 (Base case)
# Fibonacci(1) = 1 (Base case)
# Fibonacci(2) = Fibonacci(1) + Fibonacci(0) = 1 + 0 = 1
# Fibonacci(3) = Fibonacci(2) + Fibonacci(1) = 1 + 1 = 2
# Fibonacci(4) = Fibonacci(3) + Fibonacci(2) = 2 + 1 = 3
# Fibonacci(5) = Fibonacci(4) + Fibonacci(3) = 3 + 2 = 5
# Fibonacci(6) = Fibonacci(5) + Fibonacci(4) = 5 + 3 = 8
# Fibonacci(7) = Fibonacci(6) + Fibonacci(5) = 8 + 5 = 13
# Fibonacci(8) = Fibonacci(7) + Fibonacci(6) = 13 + 8 = 21
# Fibonacci(9) = Fibonacci(8) + Fibonacci(7) = 21 + 13 = 34

# def fibonacci(n):
#     if n<0:
#         print("incorrect-number") # fibonacci is only for +ve integers
#     elif n==0:
#         return 0
#     elif n==1 or n==2:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# n=9
# print("Fibonacci number of n is:",fibonacci(n))