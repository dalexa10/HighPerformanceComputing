import time

def factorial(n):
    fact = 1
    for x in range(2, n+1):
        fact = fact * x
    return fact

# Timing function
start = time.time()
factorial(400000)
end = time.time()
print('Operation done in {} seconds'.format(end - start))


