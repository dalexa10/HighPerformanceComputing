from threading import Thread

def func1(length):
    sum_f1 = 0
    for x in range(0, length):
        sum_f1 += x
    print('Sum is {}'.format(sum_f1))

def func2(length):
    """ Computes the sum of squares"""
    sum_f2 = 0
    for x in range(0, length):
        sum_f2 += x * x
    print('Sum of squares is {}'.format(sum_f2))

def func3(length):
    """ Computes the sum of cubes"""
    sum_f3 = 0
    for x in range(0, length):
        sum_f3 += x ** 3
    print('Sum of cubes is {}'.format(sum_f3))

# Threading part
def do_threading():
    length = 3
    thread_simple = Thread(target=func1, args=(length,))
    thread_square = Thread(target=func2, args=(length,))
    thread_cube = Thread(target=func3, args=(length,))

    # Start Execution
    thread_simple.start()
    thread_square.start()
    thread_cube.start()

    # Call the joint function
    thread_simple.join()
    thread_square.join()
    thread_cube.join()


do_threading()
