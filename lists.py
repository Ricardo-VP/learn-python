demo_list = [1, 'hello', 1.34, True, [1,2,3]]
colors = ['red', 'green', 'blue']

numbers_list = list((1, 2, 3))
# print(numbers_list)

range_list = list(range(1, 10)) 
# print(range_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# List methods
# print(dir(colors))

# 1. Length
print(len(colors))

# 2. X Position
print(colors[1]) # green

# 3. -X Position
print(colors[-1]) # blue

# 4. Find element
print('green' in colors) # True

# 5. Change element
colors[0] = 'yellow'
print(colors) # ['yellow', 'green', 'blue']

# 6. Append element
colors.append('violet')
print(colors) # ['yellow', 'green', 'blue', 'violet']

# 7. Extend (add +1)
colors.extend(['white', 'black']) # or ('white', 'black')
print(colors)
# ['yellow', 'green', 'blue', 'violet', 'white', 'black']

# 8. Insert
colors.insert(len(colors), 'orange')
print(colors)
# ['yellow', 'green', 'blue', 'violet', 'white', 'black', 'orange']

# 8. Pop
colors.pop()
print(colors)
# ['yellow', 'green', 'blue', 'violet', 'white', 'black']

# 9. Remove
colors.remove('black')
print(colors)
# ['yellow', 'green', 'blue', 'violet', 'white']

# 10. Pop with index
colors.pop(len(colors)-1)
print(colors)
# ['yellow', 'green', 'blue', 'violet']

# 11. Sort
colors.sort()
print(colors)
# ['blue', 'green', 'violet', 'yellow']

# 12. Sort invert
colors.sort(reverse=True)
print(colors)
# ['yellow', 'violet', 'green', 'blue']

# 13. Get index
print(colors.index('yellow'))
# 0

# 14. Count element
colors.append('yellow')
print(colors.count('yellow'))
# 2

# 11. Clear
colors.clear()
print(colors)
# []

