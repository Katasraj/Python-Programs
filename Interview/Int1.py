'''Find the words ge 4 in a given sentence'''

'''
s = "Please subscrive channel and like videos"

r = s.split(" ")
for i in r:
    if len(i) <=4:
        print(i)
'''
#####################################################################################################################
'''Palindrome Check'''
# def palindromeCheck1(i = input("Enter a word: ")):
#     r = i[::-1]
#     if i == r:
#         return True
#     else:
#         return False
#print(palindromeCheck1())

# def palindromeCheck2(j = input("Enter a word: ")):
#     t = ''
#     for w in j:
#         t = w+t
#     if j == t:
#         return True
#     else:
#         return False
# print(palindromeCheck2())
#####################################################################################################################
'''
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

# keys_list = list(sample_dict.keys())
# d = sample_dict[keys_list[2]]
# d['salary'] = 8500
# print(sample_dict)
sample_dict['emp3']['salary'] = 8500
print(sample_dict)
'''
#####################################################################################################################
'''Get Value for minimum value of Key in a dictonary'''
# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
#
# def get_min_value(l):
#     min = l[0]
#     for i in l:
#         if i<min:
#             min = i
#     return min
#
# dict_vals = [v for k,v in sample_dict.items()]
# print({i for i in sample_dict if sample_dict[i] == get_min_value(dict_vals)})
# print(min(sample_dict, key=sample_dict.get))
#####################################################################################################################
'''Write a program to rename a key city to a location in the dictionary'''
# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
#
# print(sample_dict)
# lst = list(sample_dict.keys())
# for i in lst:
#     if i == 'city':
#         sample_dict['location'] = sample_dict['city']
#         del(sample_dict['city'])
#         break
#
# print(sample_dict)
#
# print([i for i in sample_dict if sample_dict[i] == 'New york'])

#####################################################################################################################
'''Check if a value exists in a dictionary'''
# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# print(list(sample_dict.values()))
#
# #print(['value 200 exists' for i in sample_dict if sample_dict[i] == 200][0])
# print(['Value 200 exists' if 200 in sample_dict.values() else 'Value 200 does not exist'][0])
#####################################################################################################################
'''List Comprehensions'''
print([['Even' if i%2==0 else 'Odd' for i in range(1,10)] for j in range(3)])

print([[i for i in range(1,10)][j:j+3] for j in range(0,9,3)])

l = [15,21,35,3,6,10,23,78,54,71,100,12,2,102]
l.sort()
print([l[j:j+3] for j in range(0,9,3)])
