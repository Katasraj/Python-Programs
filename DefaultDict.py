from collections import defaultdict

'''
The functionality of both dictionaries and defaultdict is almost the same except for the fact 
that defaultdict never raises a KeyError. It provides a default value for the key that does 
not exist
'''

'''
You can pass like int, list, or dict, which defaultdict will call to create a default value.
'''

my_dict = defaultdict(list)
print(my_dict)


my_dict['Fruits'] = 'Apple'
my_dict['Vegetable'] = 'Onion'

print(my_dict)

print(100*'*')

count = defaultdict(int)

#items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

items = "Nagamurali"

for i in items:
    count[i] += 1

print(count)

for k,v in count.items():
    print(v," times ",k)

