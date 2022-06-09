# "def" define a function
def hello(name = "person"):
    print('Hello', name)

hello("Ricardo") # Hello Ricardo
hello() # Hello person

def add(number_one, number_two):
    print(number_one + number_two)

add(5, 10) # 15

# labmda functions

add_lambda = lambda number_one, number_two: number_one + number_two

print(add_lambda(10, 30)) # 40