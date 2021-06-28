import re

#The search() function returns a Match object:

txt = "@.com"
x = re.search("([a-zA-Z0-9]+@|@)+[a-zA-Z0-9]+(.com|.in|.net|.co.in)", txt)
print(x)

