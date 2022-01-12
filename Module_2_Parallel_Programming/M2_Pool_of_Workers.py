import time
from multiprocessing import Pool


def some_function(x):
    """ This can be any function """
    return x**2 + x + 3


start1 = time.time()
for i in range(0, 30000000):
    some_function(i)
end1 = time.time()
print("Time taken is {}".format(end1 - start1))


# Using Pool of Workers
start2 = time.time()
pool = Pool(processes=8)
input_list = range(0, 30000000)
result2 = pool.map(some_function, input_list) # This issues a blocking call
end2 = time.time()
print('Time taken is {}'.format(end2 - start2))


start3 = time.time()
pool = Pool(processes=8)
input_list = range(0, 30000000)
# This issues a non blocking call (Running multiple process at the time)
# Use this when you know that the processes are independent of each other
result3 = pool.map_async(some_function, input_list)
end3 = time.time()
print('Time taken is {}'.format(end3 - start3))
