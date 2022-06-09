from turtle import color

colors = {'red', 'green', 'blue'}

print(type(colors)) # set

# Find element
print('red' in colors) # True

# Add element
colors.add('black') # Random position
print(colors)

# Remove element
colors.remove('red')
print(colors)

# Clear
colors.clear()
print(colors) # set()