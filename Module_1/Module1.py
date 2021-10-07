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




