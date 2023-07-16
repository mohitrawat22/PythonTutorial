# string can be single quotes
str1 = 'world'
# string can be double quotes
str1 = "world"

print('Planet name is earth')
print("Planet name is earth")
print('Planet name is "earth"')
print("Planet name is 'earth'")

# multiline string
# 3 single or double quotes
str1 = '''My name is Mohit
My planet name is earth'''
print(str1)

str2 = "earth"
print(str2)

# character at particular index
print('character at index 2 is: '+str2[2])

# loop the string
for i in str2:
    print(i)

str3 = "hello world"


# string slicing

# index 0 to 6, not including index 7
print(str3[0: 7])
# index 0 to 6, not including index 7
print(str3[: 7])
# index 2 to last index
print(str3[2: ])
# index 2 to 6, not including index 7
print(str3[2: 7])
# index 0 to len-2
print(str3[0: -2])
# index len-2 to len-4
print(str3[-2: -4])
# index len-4 to len-2
print(str3[-4: -2])


# string functions

str4 = "!!!Hello!!!World!!!Hello!!!"
# length of str4
print(len(str4))
str4 = str4.rstrip("!")
print(str4)
str4 = str4.lstrip("!")
print(str4)
print(str4.upper())
print(str4.lower())
print(str4.capitalize())
print(str4.replace("Hello", "Earth"))
print(str4.split("!!!"))
print(str4.center(50))
print(str4.count("Hello"))
print(str4.startswith("Hel"))
print(str4.endswith("lo"))
print(str4.endswith("lo", 2, 6))
print(str4.find("Wo"))
print(str4.index("lo"))
print(str4.isalnum())

str5 = "    "
print(str5.isspace())
str5 = "    "
print(str5.isspace())

str6 = "Hello World"
print(str6.istitle())
str6 = "Hello world"
print(str6.istitle())
print(str6.swapcase())
print(str6.title())

# f-string
letter = "My name is {} and country is {}"
country = 'India'
name = 'Mohit'

print(letter.format(name, country))
print(letter.format(country, name))

letter = "My name is {0} and country is {1}"
print(letter.format(name, country))
letter = "My name is {1} and country is {0}"
print(letter.format(country, name))

print(f"My name is {name} and country is {country}")
print("price is {price:.2f}".format(price=45.6666))
print(f"{2+6}")

# docstring
def add(a, b):
    '''function is to add two numbers'''
    print(a+b)

# when you hover over a add function, it will show docstring
add(3,6)
print(add.__doc__)
