''' Exercise 3.1. Write a function named right_justify that takes a string named s as a parameter
 and prints the string with enough leading spaces so that the last letter of the string is in column 70
 of the display.
 >>> right_justify('monty')
 monty
 Hint: Use string concatenation and repetition. Also, Python provides a built-in function called len
 that returns the length of a string, so the value of len('monty') is 5.
'''

def right_justify(s):
    spaces = 70 - len(s)
    print(" " * spaces + s)
right_justify("parthh")


'''' Exercise 3.2. A function object is a value you can assign to a variable or pass as an argument. For
 example, do_twice is a function that takes a function object as an argument and calls it twice:
 def do_twice(f):
 f()
 f()
 Here’s an example that uses do_twice to call a function named print_spam twice.
 def print_spam():
 print('spam')
 do_twice(print_spam)
 1. Type this example into a script and test it.
 2. Modify do_twice so that it takes two arguments, a function object and a value, and calls the
 function twice, passing the value as an argument.
 3. Copy the definition of print_twice from earlier in this chapter to your script.
 4. Use the modified version of do_twice to call print_twice twice, passing 'spam' as an
 argument.
 5. Define a new function called do_four that takes a function object and a value and calls the
 function four times, passing the value as a parameter. There should be only two statements in
 the body of this function, not four.'''

"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""




# def do_twice(func, arg):
#     """Runs a function twice.

#     func: function object
#     arg: argument passed to the function
#     """
#     func(arg)
#     func(arg)


# def print_twice(arg):
#     """Prints the argument twice.

#     arg: anything printable
#     """
#     print(arg)
#     print(arg)


# def do_four(func, arg):
#     """Runs a function four times.

#     func: function object
#     arg: argument passed to the function
#     """
#     do_twice(func, arg)
#     do_twice(func, arg)


# do_twice(print, 'spam')
# print('')

# do_four(print, 'spam')


''' Note: This exercise should be done using only the statements and other features we
 have learned so far.
 1. Write a function that draws a grid like the following:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
 
 Hint: to print more than one value on a line, you can print a comma-separated sequence of
 values:
 print('+', '-')
 By default, print advances to the next line, but you can override that behavior and put a
 space at the end, like this:
 print('+', end=' ')
 print('-')
'''

def horizontal():
    print('+', '- ' * 4, '+', '- '  * 4,  '+')



def vertical():
    print('|', ' ' * 8, '|', ' ' * 8,'|')
    print('|', ' ' * 8, '|', ' ' * 8,'|')
    print('|', ' ' * 8, '|', ' ' * 8,'|')
    print('|', ' ' * 8, '|', ' ' * 8,'|')
    
def draw_grid():
    horizontal()
    vertical()
    horizontal()
    vertical()
    horizontal()
draw_grid()    
   