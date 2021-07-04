# region Strings

# Strings

# %% Example
print("Hello")
print('Hello')


# Assign String to a Variable

# %% Example
a = "Hello"
print(a)


# Multiline Strings

# %% Example
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# %% Example
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


# Strings are Arrays

# %% Example
a = "Hello, World!"
print(a[1])


# Looping Through a String

# %% Example
for x in "banana":
    print(x)


# String Length

# %% Example
a = "Hello, World!"
print(len(a))


# Check String

# %% Example
txt = "The best things in life are free!"
print("free" in txt)

# %% Example
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")


# Check if NOT

# %% Example
txt = "The best things in life are free!"
print("expensive" not in txt)

# %% Example
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("Yes, 'expensive' is NOT present.")

# endregion


# region Slicing Strings

# Slicing

# %% Example
b = "Hello, World!"
print(b[2:5])


# Slice From the Start

# %% Example
b = "Hello, World!"
print(b[:5])


# Slice To the End

# %% Example
b = "Hello, World!"
print(b[2:])


# Negative Indexing

# %% Example
b = "Hello, World!"
print(b[-5:-2])

# endregion


# region Modify Strings

# Upper Case

# %% Example
# The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())


# Lower Case

# %% Example
# The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())


# Remove Whitespace

# %% Example
# The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip())  # returns "Hello, World!"


# Replace String

# %% Example
# The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))


# Split String

# %% Example
# The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(","))  # returns ['Hello', ' World!']

# endregion


# region String Concatenation

# String Concatenation

# %% Example
a = "Hello"
b = "World"
c = a + b
print(c)

# %% Example
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# endregion


# region Format - Strings

# String Format

# %% Example
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# %% Example
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# %% Example
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# endregion


# region Escape Characters

# Escape Characters

# %% Example
# The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north."

# %% Example
# Code: \' , Result: Single Quote
txt = 'It\'s alright.'
print(txt)

# %% Example
# Code: \b , Result: Backslash
txt = "This will insert one \\ (backslash)."
print(txt)

# %% Example
# Code: \n , Result: New Line
txt = "Hello\nWorld!"
print(txt)

# %% Example
# Code: \r , Result: Carriage Return
txt = "Hello\rWorld!"
print(txt) 

# %% Example
# Code: \t , Result: Tab
txt = "Hello\tWorld!"
print(txt)

# %% Example
# Code: \b , Result: Backspace
# This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt)

# %% Example
# Code: \f , Result: Form Feed

# %% Example
# Code: \ooo , Result: Octal value
# A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt)

# %% Example
# Code: \xhh , Result: Hex value
# A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 

# endregion


# region String Methods

# Note: All string methods returns new values. They do not change the original string.


# String capitalize() Method
# The capitalize() method returns a string where the first character is upper case.

# %% Example
# Upper case the first letter in this sentence:
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)
# Out: Hello, and welcome to my world.


# String casefold() Method
# The casefold() method returns a string where all the characters are lower case.

# %% Example
# Make the string lower case:
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)
# Out: hello, and welcome to my world!


# String center() Method
# The center() method will center align the string, using a specified character (space is default) as the fill character.

# %% Example
# Print the word "banana", taking up the space of 20 characters, with "banana" in the middle:
txt = "banana"
x = txt.center(20)
print(x)
# Out:        banana

# %% Example
txt = "banana"
x = txt.center(20, "O")
print(x)
# Out: OOOOOOObananaOOOOOOO


# String count() Method
# The count() method returns the number of times a specified value appears in the string.

# %% Example
# Return the number of times the value "apple" appears in the string:
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)
# Out: 2

# %% Example
# Search from position 10 to 24:
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x)
# Out: 1


# String encode() Method
# The encode() method encodes the string, using the specified encoding. 
# If no encoding is specified, UTF-8 will be used.

# %% Example
# UTF-8 encode the string:
txt = "My name is Ståle"
x = txt.encode()
print(x)
# Out: b'My name is St\xc3\xa5le'

# %% Example
# These examples uses ascii encoding, and a character that cannot be encoded, showing the result with different errors:
txt = "My name is Ståle"
print(txt.encode(encoding="ascii",errors="backslashreplace"))
# Out: b'My name is St\\xe5le'
print(txt.encode(encoding="ascii",errors="ignore"))
# Out: b'My name is Stle'
print(txt.encode(encoding="ascii",errors="namereplace"))
# Out: b'My name is St\\N{LATIN SMALL LETTER A WITH RING ABOVE}le'
print(txt.encode(encoding="ascii",errors="replace"))
# Out: b'My name is St?le'
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))
# Out: b'My name is St&#229;le'


# String endswith() Method
# The endswith() method returns True if the string ends with the specified value, otherwise False.

# %% Example
# Check if the string ends with a punctuation sign (.):
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)
# Out: True

# %% Example
# Check if the string ends with the phrase "my world.":
txt = "Hello, welcome to my world."
x = txt.endswith("my world.")
print(x)
# Out: True

# %% Example
# Check if position 5 to 11 ends with the phrase "my world.":
txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11)
print(x)
# Out: False


# String expandtabs() Method
# The expandtabs() method sets the tab size to the specified number of whitespaces.

# %% Example
# Set the tab size to 2 whitespaces:
txt = "H\te\tl\tl\to"
x = txt.expandtabs(2)
print(x)
# Out: H e l l o

# %% Example
# See the result using different tab sizes:
txt = "H\te\tl\tl\to"
print(txt)
# Out: H	e	l	l	o
print(txt.expandtabs())
# Out: H	e	l	l	o
print(txt.expandtabs(2))
# Out: H e l l o
print(txt.expandtabs(4))
# Out: H   e   l   l   o
print(txt.expandtabs(10))
# Out: H         e         l         l         o


# String find() Method
# The find() method finds the first occurrence of the specified value.
# The find() method returns -1 if the value is not found.
# The find() method is almost the same as the index() method, 
# the only difference is that the index() method raises an exception if the value is not found.

# %% Example
# Where in the text is the word "welcome"?:
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)
# Out: 7

# %% Example
# Where in the text is the first occurrence of the letter "e"?:
txt = "Hello, welcome to my world."
x = txt.find("e")
print(x)
# Out: 1

# %% Example
# Where in the text is the first occurrence of the letter "e" when you only search between position 5 and 10?:
txt = "Hello, welcome to my world."
x = txt.find("e", 5, 10)
print(x)
# Out: 8

# %% Example
# If the value is not found, the find() method returns -1, but the index() method will raise an exception:
txt = "Hello, welcome to my world."
print(txt.find("q"))
# Out: -1
print(txt.index("q"))
# Out: ValueError: substring not found


# String format() Method
# The format() method formats the specified value(s) and insert them inside the string's placeholder.
# The format() method returns the formatted string.

# %% Example
# Insert the price inside the placeholder, the price should be in fixed point, two-decimal format:
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
# Out: For only 49.00 dollars!

# %% Example
txt1 = "My name is {fname}, I'm {age}".format(fname="John", age=36)
print(txt1)
# Out: My name is John, I'm 36
txt2 = "My name is {0}, I'm {1}".format("John",36)
print(txt2)
# Out: My name is John, I'm 36
txt3 = "My name is {}, I'm {}".format("John",36)
print(txt3)
# Out: My name is John, I'm 36

# %% Example
# :<  Left aligns the result (within the available space)
txt = "We have {:<8} chickens."
print(txt.format(49))
# Out: We have 49       chickens.

# %% Example
# :>  Right aligns the result (within the available space)
txt = "We have {:>8} chickens."
print(txt.format(49))
# Out: We have       49 chickens.

# %% Example
# :^  Center aligns the result (within the available space)
txt = "We have {:^8} chickens."
print(txt.format(49))
# Out: We have    49    chickens.

# %% Example
# :=  Places the sign to the left most position
txt = "The temperature is {:=8} degrees celsius."
print(txt.format(-5))
# Out: The temperature is -      5 degrees celsius.

# %% Example
# :+  Use a plus sign to indicate if the result is positive or negative
txt = "The temperature is between {:+} and {:+} degrees celsius."
print(txt.format(-3, 7))
# Out: The temperature is between -3 and +7 degrees celsius.

# %% Example
# :-  Use a minus sign for negative values only
txt = "The temperature is between {:-} and {:-} degrees celsius."
print(txt.format(-3, 7))
# Out: The temperature is between -3 and 7 degrees celsius.

# %% Example
# :  Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
txt = "The temperature is between {: } and {: } degrees celsius."
print(txt.format(-3, 7))
# Out: The temperature is between -3 and  7 degrees celsius.

# %% Example
# :,  Use a comma as a thousand separator
txt = "The universe is {:,} years old."
print(txt.format(13800000000))
# Out: The universe is 13,800,000,000 years old.

# %% Example
# :_  Use a underscore as a thousand separator
txt = "The universe is {:_} years old."
print(txt.format(13800000000))
# Out: The universe is 13_800_000_000 years old.

# %% Example
# :b  Binary format
txt = "The binary version of {0} is {0:b}"
print(txt.format(5))
# Out: The binary version of 5 is 101

# %% Example
# :c  Converts the value into the corresponding unicode character

# %% Example
# :d  Decimal format
txt = "We have {:d} chickens."
print(txt.format(0b101))
# Out: We have 5 chickens.

# %% Example
# :e  Scientific format, with a lower case e
txt = "We have {:e} chickens."
print(txt.format(5))
# Out: We have 5.000000e+00 chickens.

# %% Example
# :E  Scientific format, with an upper case E
txt = "We have {:E} chickens."
print(txt.format(5))
# Out: We have 5.000000E+00 chickens.

# %% Example
# :f  Fix point number format
txt = "The price is {:.2f} dollars."
print(txt.format(45))
# Out: The price is 45.00 dollars.
txt = "The price is {:f} dollars."
print(txt.format(45))
# Out: The price is 45.000000 dollars.

# %% Example
# :F  Fix point number format, in uppercase format (show inf and nan as INF and NAN)
x = float('inf')

txt = "The price is {:F} dollars."
print(txt.format(x))
# Out: The price is INF dollars.
txt = "The price is {:f} dollars."
print(txt.format(x))
# Out: The price is inf dollars.

# %% Example
# :g  General format

# %% Example
# :G  General format (using a upper case E for scientific notations)

# %% Example
# :o  Octal format
txt = "The octal version of {0} is {0:o}"
print(txt.format(10))
# Out: The octal version of 10 is 12

# %% Example
# :x  Hex format, lower case
txt = "The Hexadecimal version of {0} is {0:x}"
print(txt.format(255))
# Out: The Hexadecimal version of 255 is ff

# %% Example
# :X  Hex format, upper case
txt = "The Hexadecimal version of {0} is {0:X}"
print(txt.format(255))
# Out: The Hexadecimal version of 255 is FF

# %% Example
# :n  Number format

# %% Example
# :%  Percentage format
txt = "You scored {:%}"
print(txt.format(0.25))
# Out: You scored 25.000000%
txt = "You scored {:.0%}"
print(txt.format(0.25))
# Out: You scored 25%


# String format_map() Method
# Formats specified values in a string


# String index() Method
# The index() method finds the first occurrence of the specified value.
# The index() method raises an exception if the value is not found.
# The index() method is almost the same as the find() method, 
# the only difference is that the find() method returns -1 if the value is not found.

# %% Example
# Where in the text is the word "welcome"?:
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)
# Out: 7

# %% Example
# Where in the text is the first occurrence of the letter "e"?:
txt = "Hello, welcome to my world."
x = txt.index("e")
print(x)
# Out: 1

# %% Example
# Where in the text is the first occurrence of the letter "e" when you only search between position 5 and 10?:
txt = "Hello, welcome to my world."
x = txt.index("e", 5, 10)
print(x)
# Out: 8

# %% Example
# If the value is not found, the find() method returns -1, but the index() method will raise an exception:
txt = "Hello, welcome to my world."
print(txt.find("q"))
# Out: -1
print(txt.index("q"))
# Out: ValueError: substring not found


# String isalnum() Method
# The isalnum() method returns True if all the characters are alphanumeric, 
# meaning alphabet letter (a-z) and numbers (0-9).

# %% Example
# Check if all the characters in the text are alphanumeric:
txt = "Company12"
x = txt.isalnum()
print(x)
# Out: True

# %% Example
# Check if all the characters in the text is alphanumeric:
txt = "Company 12"
x = txt.isalnum()
print(x)
# Out: False


# String isalpha() Method
# The isalpha() method returns True if all the characters are alphabet letters (a-z).

# %% Example
# Check if all the characters in the text are letters:
txt = "CompanyX"
x = txt.isalpha()
print(x)
# Out: True

# %% Example
# Check if all the characters in the text is alphabetic:
txt = "Company10"
x = txt.isalpha()
print(x)
# Out: False


# String isdecimal() Method
# The isdecimal() method returns True if all the characters are decimals (0-9).

# %% Example
# Check if all the characters in the unicode object are decimals:
txt = "\u0033" #unicode for 3
x = txt.isdecimal()
print(x)
# Out: True

# %% Example
# Check if all the characters in the unicode are decimals:
a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G

print(a.isdecimal())
# Out: True
print(b.isdecimal())
# Out: False


# String isdigit() Method
# The isdigit() method returns True if all the characters are digits, otherwise False.

# %% Example
# Check if all the characters in the text are digits:
txt = "50800"
x = txt.isdigit()
print(x)
# Out: True

# %% Example
# Check if all the characters in the text are digits:
a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²

print(a.isdigit())
# Out: True
print(b.isdigit())
# Out: True


# String isidentifier() Method
# The isidentifier() method returns True if the string is a valid identifier, otherwise False.
# A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). 
# A valid identifier cannot start with a number, or contain any spaces.

# %% Example
# Check if the string is a valid identifier:
txt = "Demo"
x = txt.isidentifier()
print(x)
# Out: True

# %% Example
# Check if the strings are valid identifiers:
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())
# Out: True
print(b.isidentifier())
# Out: True
print(c.isidentifier())
# Out: False
print(d.isidentifier())
# Out: False


# String islower() Method
# The islower() method returns True if all the characters are in lower case, otherwise False.
# Numbers, symbols and spaces are not checked, only alphabet characters.

# %% Example
# Check if all the characters in the text are in lower case:
txt = "hello world!"
x = txt.islower()
print(x)
# Out: True

# %% Example
# Check if all the characters in the texts are in lower case:
a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"

print(a.islower())
# Out: False
print(b.islower())
# Out: True
print(c.islower())
# Out: False


# String isnumeric() Method
# The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.
# Exponents, like ² and ¾ are also considered to be numeric values.
# "-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric, and the - and the . are not.

# %% Example
# Check if all the characters in the text are numeric:
txt = "565543"
x = txt.isnumeric()
print(x)
# Out: True

# %% Example
# Check if the characters are numeric:
a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for &sup2;
c = "10km2"
d = "-1"
e = "1.5"

print(a.isnumeric())
# Out: True
print(b.isnumeric())
# Out: True
print(c.isnumeric())
# Out: False
print(d.isnumeric())
# Out: False
print(e.isnumeric())
# Out: False


# String isprintable() Method
# The isprintable() method returns True if all the characters are printable, otherwise False.

# %% Example
# Check if all the characters in the text are printable:
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)
# Out: True

# %% Example
# Check if all the characters in the text are printable:
txt = "Hello!\nAre you #1?"
x = txt.isprintable()
print(x)
# Out: False


# String isspace() Method
# The isspace() method returns True if all the characters in a string are whitespaces, otherwise False.

# %% Example
# Check if all the characters in the text are whitespaces:
txt = "   "
x = txt.isspace()
print(x)
# Out: True

# %% Example
# Check if all the characters in the text are whitespaces:
txt = "   s   "
x = txt.isspace()
print(x)
# Out: False


# String istitle() Method
# The istitle() method returns True if all words in a text start with a upper case letter, 
# AND the rest of the word are lower case letters, otherwise False.
# Symbols and numbers are ignored.

# %% Example
# Check if each word start with an upper case letter:
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)
# Out: True

# %% Example
# Check if each word start with an upper case letter:
a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"

print(a.istitle())
# Out: False
print(b.istitle())
# Out: True
print(c.istitle())
# Out: True
print(d.istitle())
# Out: True


# String isupper() Method
# The isupper() method returns True if all the characters are in upper case, otherwise False.
# Numbers, symbols and spaces are not checked, only alphabet characters.

# %% Example
# Check if all the characters in the text are in upper case:
txt = "THIS IS NOW!"
x = txt.isupper()
print(x)
# Out: True

# %% Example
# Check if all the characters in the texts are in upper case:
a = "Hello World!"
b = "hello 123"
c = "MY NAME IS PETER"

print(a.isupper())
# Out: False
print(b.isupper())
# Out: False
print(c.isupper())
# Out: True


# String join() Method
# The join() method takes all items in an iterable and joins them into one string.
# A string must be specified as the separator.

# %% Example
# Join all items in a tuple into a string, using a hash character as separator:
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)
# Out: John#Peter#Vicky

# %% Example
# myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)
# Out: NameError: name 'myDict' is not defined


# String ljust() Method
# The ljust() method will left align the string, using a specified character (space is default) as the fill character.

# %% Example
# Return a 20 characters long, left justified version of the word "banana":
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")
# Out: banana               is my favorite fruit.

# %% Example
# Using the letter "O" as the padding character:
txt = "banana"
x = txt.ljust(20, "O")
print(x)
# Out: bananaOOOOOOOOOOOOOO


# String lower() Method
# The lower() method returns a string where all characters are lower case.
# Symbols and Numbers are ignored.

# %% Example
# Lower case the string:
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)
# Out: hello my friends


# String lstrip() Method
# The lstrip() method removes any leading characters (space is the default leading character to remove)

# %% Example
# Remove spaces to the left of the string:
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")
# Out: of all fruits banana      is my favorite

# %% Example
# Remove the leading characters:
txt = ",,,,,ssaaww.....banana"
x = txt.lstrip(",.asw")
print(x)
# Out: banana


# String maketrans() Method
# The maketrans() method returns a mapping table that can be used with the translate() 
# method to replace specified characters.

# %% Example
txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))
# Out: Hello Pam!

# %% Example
txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = txt.maketrans(x, y)
print(txt.translate(mytable)) 
# Out: Hi Joe!

# %% Example
# The third parameter in the mapping table describes characters that you want to remove from the string:
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = txt.maketrans(x, y, z)
print(txt.translate(mytable))
# Out: G i Joe!

# %% Example
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
print(txt.maketrans(x, y, z))
# Out: {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}


# String partition() Method
# The partition() method searches for a specified string, and splits the string into a tuple containing three elements.
# The first element contains the part before the specified string.
# The second element contains the specified string.
# The third element contains the part after the string.

# %% Example
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x) 
# Out: ('I could eat ', 'bananas', ' all day')

# %% Example
txt = "I could eat bananas all day"
x = txt.partition("apples")
print(x)
# Out: ('I could eat bananas all day', '', '')


# String replace() Method
# The replace() method replaces a specified phrase with another specified phrase.

# %% Example
# Replace the word "bananas":
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)
# Out: I like apples

# %% Example
# Replace all occurrence of the word "one":
txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three")
print(x)
# Out: three three was a race horse, two two was three too.

# %% Example
# Replace the two first occurrence of the word "one":
txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three", 2)
print(x)
# Out: three three was a race horse, two two was one too.


# String rfind() Method
# The rfind() method finds the last occurrence of the specified value.
# The rfind() method returns -1 if the value is not found.
# The rfind() method is almost the same as the rindex() method. See example below.

# %% Example
# Where in the text is the last occurrence of the string "casa"?:
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)
# Out: 12

# %% Example
# Where in the text is the last occurrence of the letter "e"?:
txt = "Hello, welcome to my world."
x = txt.rfind("e")
print(x)
# Out: 13

# %% Example
# Where in the text is the last occurrence of the letter "e" when you only search between position 5 and 10?:
txt = "Hello, welcome to my world."
x = txt.rfind("e", 5, 10)
print(x)
# Out: 8

# %% Example
# If the value is not found, the rfind() method returns -1, but the rindex() method will raise an exception:
txt = "Hello, welcome to my world."

print(txt.rfind("q"))
# Out: -1
print(txt.rindex("q"))
# Out: ValueError: substring not found

# endregion
