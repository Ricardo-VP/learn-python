myStr = 'hello world'

# print(dir(myStr)) # Print the string methods

# Uppercase
print(myStr.upper())
# Lowercase
print(myStr.lower())
# Swapcase
print(myStr.swapcase())
# Capitalize
print(myStr.capitalize())

# Replace and then upper
print(myStr.replace('hello', 'bye').upper())

# Count one letter
print(myStr.count('l'))

# Starts with
print(myStr.startswith('hello')) # True
print(myStr.startswith('Hello')) # False 
# Ends with
print(myStr.endswith('world')) # True

# Split
print(myStr.split('o')) # ['hell', ' w', 'rld'] a list of strings

# Find
print(myStr.find('o')) # 4 - index of 'o'
# Index of
print(myStr.index('e')) # 1

# Length
print(len(myStr)) # 11

# Is alphanumeric
print(myStr.isalpha()) # False

# Print x position
print(myStr[4]) # 'o'

# Print -x position
print(myStr[-5]) # 'w'

# Concat strings
print('The string is: ' + myStr)
print(f'The string is: {myStr}') # Python 3.6 >
print('The string is: {0}'.format(myStr))