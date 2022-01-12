from multiprocessing import Process

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

def do_something():
    length = 5

    # Create the processes
    process_simple = Process(target=func1, args=(length, ))
    process_square = Process(target=func2, args=(length, ))
    process_cube = Process(target=func3, args=(length, ))

    # Start the process
    process_simple.start()
    process_square.start()
    process_cube.start()

    # Wait for the processes to end
    process_simple.join()
    process_square.join()
    process_cube.join()

do_something()
