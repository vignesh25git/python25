num1 = int(input("Enter the number1"))
num2 = int(input("Enter the number2"))

try:
    num3 = num1 / num2
    print(f'{num1} divided by {num2} is {num3}')
except ZeroDivisionError:
    print(f'{num1} divided by {num2} is infinity')

"""
ZeroDivisionError   Dividing a number by zero   10 / 0
ValueError          Invalid value for a function (e.g. int("abc"))   int("hello")
TypeError           Wrong data type used in operation   "abc" + 10
IndexError          Accessing out-of-range list index   my_list[10]
KeyError            Accessing a non-existing key in a dictionary   my_dict["not_found"]
AttributeError      Accessing a non-existing attribute of an object   None.upper()
FileNotFoundError   File not found when opening   open("abc.txt")
ImportError         Trying to import a missing module   import nomodule
NameError           Using a variable that was never defined   print(xyz)
IndentationError    Incorrect indentation   Code not properly indented
SyntaxError         Writing invalid Python code   if True print("hi")
RuntimeError        Generic error not falling into other categories   Rare cases
StopIteration       Raised by next() when iterator is exhausted   In loops and generators
MemoryError         Program runs out of memory   Working with huge data
RecursionError      Too many recursive calls   A function calls itself endlessly
"""



