'''
Strings can be an array of characters and thus be accessed like an array
for ex:
Name = "Bob"
Name[0] = "B"
len(Name) = 3
Last index = len(Name) - 1 => 2

You can also access the characters via negative index.
Ex:
Name[-1]: b
Name[-3]: B

Note: spaces in str count as characters

Name = "Barbara Banks"
Name[0:4] = Barb
Name[8:12] = Bank
Name[starting_index:length_subarray]

Slicing:
Name[::2] = BraaBns => takes out every other letter
Name[0:5:2] = Bra => takes first five characters and slices every other char

Concatenating or concatenation:
Name = "Bob"
Statement = Name + " is the best"
print(Statement)
Note: Make sure to add space char on either Name or statement end otherwise you get...
Bobis the best

Tuples:
You can duplicate the str to create a larger str
str = 3*"Bob "
print(str)

In python, you cannot change the char at indexes of the string, you can only create a new string all together
Strings are immutable.
For ex:
You cannot do:
Name = "Bob"
Name[0] = Y
print(Name)

You have to do:
Name = "Bob"
Name = "Yob"

Escape Sequences:
- \\ indicates escape character/sequence
- because back slash is a special character, you have to do double black slash in strings
- These are for specially formatted strings
Ex:
print("Bob\nthe builder")

Escape Sequences:
\\ or print(r"Bob\ the builder") => placing an r before the string
\t
\n

String methods:

Other ways of printing:
a = "Bob"
print("before upper:", a)
=> before upper:Bob

Both return a new string
upper()
lower()

A = "Bob"
B = A.upper()
print(B) => BOB

replace()
A = "Bob the"
B = A.replace("Bob","Billard")
print(B) => "Billard the"

find()
A = "Bob the"
A.find("th") => 4
returns the first index of the sequence
If the substring is not found, then the method will return -1

String interpolation (f-strings):
name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")
=> My name is John and I am 30 years old.

str.format() Method:
name = "John"
age = 50
print("My name is {} and I am {} years old.".format(name, age))

% Operatpr: Older method, found in C language
name = "Johnathan"
age = 30
print("My name is %s and I am %d years old." % (name, age))

%s = placeholder for str
%d = placeholder for int

Of the methods, f-string is most modern and preferred in python

Other capability of f-string: You can do operations in curly braces
print(f"The sum of x and y is {x+y}.")

Raw string:
regular_string = "C:\new_folder\file.txt"
print("Regular String:", regular_string)
=> This will print: 

Regular String:  C:
ew_folderile.txt

Becuase of backslashes in file name, they will be interpreted as escape characters and
will print wrong.

raw_string = r"C:\new_folder\file.txt"
print("Raw String:", raw_string)
=> raw_string = r"C:\new_folder\file.txt"
print("Raw String:", raw_string)

(I am realizing at this point that notetaking in python is not best method due to backslashes in comments lol)

Split method
- returns a list of substrings
- Unless delimiter is specified, string is split by an whitespace
- maxsplit is the max number of splits in a string and is optional

str = "Bob the builder"
str.split(delimiter, maxsplit)
list = str => ["Bob","the","builder"] 

Regex is a whole other topic that will be put into regex notebook

'''
