import re

str1 = 'world1 Dan world2 Pan world3 Can world4 tan world5 worldan world6'
pattern = '[A-Za-z]+an'

# searches for first occurance only
match = re.search(pattern, str1)
#print(match)
#print(type(match))
#print(match.span())
#print(type(match.span()))


matches = re.finditer(pattern, str1)
for match in matches:
    print(match)
    print(match.span())
    # prints tuple
    #print(type(match.span()))
    print(str1[match.span()[0]: match.span()[1]])
