# Assignment #11: 

# Exercise 1: Simple Function
# 1.  Create a function named greet_user that takes a user's name as a parameter and prints a personalized greeting message like "Hello, [name]!".
def greet_user():
    print(f"Hello {user_name}!")

user_name = input("Enter your name")

greet_user()


# Exercise 2: Area of a Rectangle
# 1.  Create a function named calculate_rectangle_area that takes the width and height of a rectangle as parameters and returns its area.
# 2.  Demonstrate the usage of this function by calculating the area of a rectangle with width=5 and height=8.

def calculate_rectangle_area(width,height):

    print(f"This rectangle is {width*height} cm square")

width_of_rectangle = 5
height_of_rectangle = 8

calculate_rectangle_area(width_of_rectangle,height_of_rectangle)


# Exercise 3: Celsius to Fahrenheit Conversion
# 1.  Create a function named celsius_to_fahrenheit that takes a temperature in Celsius as a parameter and returns its
# equivalent temperature in Fahrenheit using the formula: Fahrenheit = (Celsius * 9/5) + 32.
# 2.  Demonstrate the usage of this function by converting a temperature of 25 degrees Celsius to Fahrenheit.

def celsius_to_fahrenheit(Celsius_degree):

    fahrenheit = (Celsius * 9 / 5) + 32
    print(f"{Celsius} Celsius degree is equal to {fahrenheit} fahrenheit degree")

Celsius= 25
celsius_to_fahrenheit(Celsius)

# Exercise 4: Check Even or Odd
# 1.  Create a function named is_even that takes an integer as a parameter and returns True if the number is even, otherwise False.
# 2.  Demonstrate the usage of this function by checking whether the number 10 is even or odd.

def is_even(number):
    if number %2 ==0:
        print(f"{number} is even number")
    else:
        print(f"{number} is not even number")

user_input_number = 10

is_even(user_input_number)


# Exercise 5: Maximum of Two Numbers
# 1.  Create a function named max_of_two that takes two numbers as parameters and returns the larger of the two.
# 2.  Demonstrate the usage of this function by finding the maximum of 32 and 78.

def max_of_two(x, y):
    if x > y:
        print(f"{x} is the maximum number")
    elif y > x:
        print(f"{y} is the maximum number")


x = 32

y = 78

max_of_two(x, y)

# Exercise 6: Vowel Checker
# 1.  Create a function named is_vowel that takes a character (a single letter) as a parameter and returns True if it's a vowel (a, e, i, o, u - both uppercase and lowercase),
# otherwise False.
# 2.  Demonstrate the usage of this function by checking whether the characters 'a', 'b', 'E', and 'Z' are vowels.


def is_vowel(characters):

    for x in characters:
        if x in vowel_letters:
            print(f"{x} it's a vowel")
        else:
            print(f"{x} This is not a vowel")

set_of_characters = ('a', 'b', 'E','Z')

vowel_letters = ("a","e",'i','o',"u","A","E","U","I","O")

is_vowel(set_of_characters)



# Exercise 7: Factorial of a Number
# 1.  Create a function named factorial that takes a positive integer as a parameter and returns its factorial. The factorial of a non-negative integer n is
# the product of all positive integers less than or equal to n.
# 2.  Demonstrate the usage of this function by calculating the factorial of 5.

n=5
def factorial(external_n):
    result = 1
    i = 1
    while i <= n:
        result = result * i
        print(result)
        i += 1


factorial(n)

# Exercise 8: Palindrome Checker
# 1.  Create a function named is_palindrome that takes a string as a parameter and returns True if it's a palindrome, otherwise False.
# A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.
# 2.  Demonstrate the usage of this function by checking whether the strings "radar" and "Python" are palindromes.
def is_palindrome(string1, string2):
    reversed_string1 = string1[::-1]
    check = string2 == reversed_string1
    print(check)

string1 = "radar"
string2 = "Python"
is_palindrome(string1, string2)


# Exercise 9: Multiples Sum
# 1.  Create a function named sum_multiples that takes an integer n as a parameter and returns the sum of all multiples of 3 and 5 that are less than n.
# 2.  Demonstrate the usage of this function by calculating the sum of multiples of 3 and 5 less than 100.

n=5
def sum_multiples(n):
    if n%3==0 or n%5==0:
        total = 1
    print(total)





# # Exercise 9: Multiples Sum
# # 1.	Create a function named sum_multiples that takes an integer n as a parameter 
# and returns the sum of all multiples of 3 and 5 that are less than n.
# # 2.	Demonstrate the usage of this function by calculating the sum of multiples 
# # of 3 and 5 less than 100.

n = 100

def sum_multiples(n):
    total = 0
    for x in range(n):
        if x%3==0 and x%5==0:
            total +=x
    print(total)

sum_multiples(n)






# Exercise 10: Print a Triangle
# 1.	Create a function named print_triangle that takes a positive integer n 
# as a parameter and prints a right-angled triangle using asterisks (*) with n rows.
# 2.	Demonstrate the usage of this function by printing a triangle with 5 rows.

n=5
def print_triangle(n):
    for x in range(1,n+1):
        print("*"*x)
print_triangle(n)

# Exercise 6: Vowel Checker
# 1.	Create a function named is_vowel that takes a character (a single letter) 
# as a parameter and returns True if it's a vowel (a, e, i, o, u - both uppercase 
# and lowercase), otherwise False.
# 2.	Demonstrate the usage of this function by checking whether the characters 
# 'a', 'b', 'E', and 'Z' are vowels.

# vowels_list = {"a","u","i","o","e","A","U","I","O","E"}

# otherlist = ("a","b","E","Z")

# for x in otherlist:
#     if x in vowels_list:
#         print(x + "  This is Vowel")
#     else:
#         print(x + "  This is not Vowel")


