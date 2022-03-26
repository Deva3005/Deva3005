print("Hello Interpreter!")
#2.1 variable for message
message = "Deva is a god damm TYRANT"
print(f"Hello Interpreter! {message.upper()}")
#2.2 variable overrider
message="Shut up"
print(message)
name = "Devavvvvv"
print("\t".join(list(name)))
import string
'''
String methods

startswith
endswith
title
capitalize
upper
lower
strip
lstrip
rstrip
ljust
rjust
center
split
find
rfind
index
rindex
join
format
replace
count

'''
#2.3 variable insertion
name=input()
print(f"Hello {name}!")
#2.4 string formatting
print(f"Hello {name}!".upper())
print(f"Hello {name}!".lower())
print(f"Hello {name}!".title())
#2.5 quotes and escape char \t \n \' \"
print(f'''
   {name} once said, “A person who never made a 
mistake never tried anything new.”
''')
#2.6 strip() method
print(f'''
   {name} once said, “A person who never made a 
mistake never tried anything new.”
'''.strip())
#2.7
print(4+4)
print(16-8)
print(8*1)
print(64/8)
print(64//8)
print(2**3)
