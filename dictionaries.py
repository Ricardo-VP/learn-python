product = {
    'name': 'book',
    'quantity': 3,
    'price': 4.99
}

person = {
    'first_name': 'Ricardo',
    'last_name': 'Vaca'
}

# print(type(product)) # dict

print(person.keys()) # dict_keys(['first_name', 'last_name'])
print(person.items()) # dict_items([('first_name', 'Ricardo'), ('last_name', 'Vaca')])

person.clear()
print(person) # {}

products = [
    {"name": "book"},
    {"name": "laptop"}
]
print(products)
# [{'name': 'book'}, {'name': 'laptop'}]