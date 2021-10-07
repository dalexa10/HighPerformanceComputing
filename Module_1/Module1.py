#%%
# ----- Lists ---------
# Operations (only important listed)
# Recall: lists are mutable objects

A = [1, 2, 3, 4, 5]
# Append
A.append(6)
# Insert
A.insert(2, 'Hi')
# Del last element
A.pop()
print(A)
# Get index from a value
print(A.index('Hi'))

#%%
# ------ Lambda Expressions ---------
# Mostly used for anonymous stuff

# Create a lambda function
sqrt_fc = lambda x: x * x
A = sqrt_fc(3)  # This parses the lambda function

# Simple addition
adder = lambda x, y: x + y
B = adder(2, 3)

#%%
# Map Lambda functions
A = [1, 2, 3, 4, 5]
sq_list = list(map(lambda x: x**2, A))
print(sq_list)

# Combine filter lambda
B = ['This', 'is', 'a', 'test']
filt_B = list(filter(lambda x: len(x) % 2 == 0, B))  # Select even-letter words
print(filt_B)

#Order a dictionary based on lambda expressions
dict_list = [{'name': 'Dario', 'age': 27},
             {'name': 'Steph', 'age': 25},
             {'name': 'Ralph', 'age': 14}]  # Note that this a list of dicts

dict_sorted = sorted(dict_list, key=lambda x: x['age'])
print(dict_sorted)

#%%
