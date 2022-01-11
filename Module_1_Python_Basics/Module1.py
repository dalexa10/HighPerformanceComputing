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
# ------------------------------------------------------------
# ------ %%%%%% 1.1 LAMBDA EXPRESSIONS %%%%%%%%%%%%%%%%% ---------
# -------------------------------------------------------------
# Mostly used for anonymous stuff

# Create a lambda function
sqrt_fc = lambda x: x * x
A = sqrt_fc(3)  # This parses the lambda function

# Simple addition
adder = lambda x, y: x + y
B = adder(2, 3)

#%%
# ----- Map Lambda Functions --------
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
# -------- Nested Lambda Expressions ---------
add_suffix = lambda suffix: (lambda my_str: my_str + " " + suffix)
add_word = add_suffix("Python!")
print(add_word("Learn"))


#%%
# ------------------------------------------------------------
# ------ %%%%%%%%%% 1.2 COMPREHENSIONS %%%%%%%%%%%%%%%%% -----
# -------------------------------------------------------------

# ----  List Comprehensions -----
# Cool Pythonic concept that will speed up your coding, as well as, your processing
my_list = [1, 2, 3, 4, 5]
nw_list = [2*i for i in my_list]
print(nw_list)


# ----- Dictionary Comprehensions ---------
dict_compre = {str(i): i**2 for i in my_list}
print(dict_compre)

# ----- Speed Up? Is it worthy? ---------
import time

start = time.time()
List_A = []
for x in range(0, 900000):
    List_A.append(x * 2)
end = time.time()
print('The time to create list A was {:.2f} seconds'.format(end - start))

start2 = time.time()
List_B = [i * 2 for i in range(0, 90000)]
end2 = time.time()
print('The time to create list B was {:.2f} seconds'.format(end2 - start2))

print('See how effective is to create list comprehensions')

#TODO  Improve timing with profiling instead ...

#%%
# --------------------------------------------------------------
# ------ %%%%%%%% 1.3 ITERATORS & GENERATORS %%%%%%%%%%%%%%%%% ----
# --------------------------------------------------------------

# 1.3.1 ITERATORS

# Iterators are objects that allow to iterate but they don't instantiate
# the whole object at the very beginning. Instead, it is created as the
# iteration is carried out, saving a lot of memory. In summarize, elements are
# created when needed, not initialized at the beginning (brute force)

class MyIter:

    def __init__(self, final_n, multiplier):
        self.final_n = final_n
        self.multiplier = multiplier

    def __iter__(self):
        self.curr = 0
        return self

    def __next__(self):
        if self.curr <= self.final_n:
            multiple = self.curr
            self.curr += self.multiplier
            return multiple
        else:
            raise StopIteration

if __name__ == '__main__':

    my_iter_init = MyIter(20, 5)  # Instantiate class
    my_iter_obj = iter(my_iter_init)  # Create iterator from the method of the class

    print(next(my_iter_obj))  # Print iterations with next method
    print(next(my_iter_obj))

    # You can try to print more elements of the iterator adding more "print(next(my_iter_obj))"

#%%
# 1.3.2 GENERATORS

# Functions that return one value at a time. They simple alternate way of creating
# iterators using Yield keyword. This keyword is used to halt/resume processing of a generator

def my_gen():
    x = 5
    y = 6
    print('Processing halted')
    yield x, y

    print('\nProcessing resumed')
    x += y
    print('\nProcessing halted')
    yield x, y

    print('\n Processing resumed')
    x += 1
    y += 10
    yield x, y

idx = 1
for c, d in my_gen():
    print('{} loop started'.format(idx))
    print(c, d)
    idx += 1


#%%
# --------------------------------------------------------------
# ---- %%%%%%%% 1.4 DECORATORS FOR TIMES ANALYSIS %%%%%%%%%%%%%%%%% ----
# --------------------------------------------------------------

#%%
# 1.4.1 DECORATORS (Part 1)
# Enhances the functionality of an existing function by taking the function by taking the function as input and
# returning a new function. They can be applied to any callable objects like function, method and classes

# Create Function
def foo():
    print("This is a normal function")

# Create Decorator
def my_decorator(my_func):
    # This function modifies the original function
    def modified_function():
        print('Start of a decorated function')
        my_func()
        print('End of a decorated function')
    # Return the modified function
    return modified_function

# Example 1
# my_new_function = my_decorator(foo)
# my_new_function()

# Another Notation
@my_decorator
def simple_function():
    print('Do nothing')
simple_function()

#%%
# 1.4.2 DECORATORS (Part 2)
# Decorators with input arguments
# Create Decorator
def my_better_decorator(my_func):
    # This function modifies the original function (adding arguments)
    def modified_function(*args, **kwargs):
        print('Start of a decorated function')
        my_func(*args, **kwargs)
        print('End of a decorated function')
    # Return the modified function
    return modified_function

@my_better_decorator
def adder(x, y):
    print('Sum of x and y is {}'.format(x+y))

adder(2, 3)

#%%
# 1.4.3 DECORATORS for Time Analysis (Part 3)
import time

def time_decorator(my_func):
    def modified_func(*args, **kwargs):
        start = time.time()
        my_func(*args, **kwargs)
        end = time.time()
        print('Time taken is {} seconds'.format(end - start))
    return modified_func

@time_decorator
def create_big_list(size):
    new_list = []
    for x in range(0, size):
        new_list.append(x)

create_big_list(100000)

@time_decorator
def create_big_list_better(size):
    return [x for x in range(0, size)]

create_big_list_better(100000)



