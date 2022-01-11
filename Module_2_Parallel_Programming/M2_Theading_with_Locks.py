from threading import Thread, Lock

# ----  Conventional Lock ------
# Locks are basically used for thread synchronization. Without them, there might be inconsistent data
# when multiple threats try to acquire the data the same time. 

thread_lock = Lock()

# Not good practice, but create a global variable
my_global_variable = 'Hello'
my_global_num = 5

def add_prefix(prefix_to_add):
    """ Add prefix to global string """
    global my_global_variable, my_global_num

    # Acquire the lock over the data shared between threads
    thread_lock.acquire()
    # Perform operation on shared data
    if my_global_num==5:
        my_global_variable = prefix_to_add + " " + my_global_variable

    # Release the lock
    thread_lock.release()

def add_suffix(suffix_to_add):
    """ Add suffix to global string"""
    global my_global_variable, my_global_num

    # Acquire the lock over the data share between threads
    thread_lock.acquire()
    # Perform operation on shared data
    my_global_num += 1
    my_global_variable = my_global_variable + " " + suffix_to_add
    # Release the lock
    thread_lock.release()

def do_threading():
    thread_prefix = Thread(target=add_prefix, args=('YOLO',))
    thread_suffix = Thread(target=add_suffix, args=('See ya',))

    thread_prefix.start()
    thread_suffix.start()

    thread_prefix.join()
    thread_suffix.join()

    global my_global_variable
    print("Final string is {}".format(my_global_variable))

do_threading()


#%% Re-entrant Lock
from threading import RLock
my_re_entrant_lock = RLock()

my_re_entrant_lock.acquire()
my_global_string = 'yolo swag'

# If this were a conventional Lock, then this would've blocked the call for the thread
# Even though the same thread is trying to be accessed again
my_re_entrant_lock.acquire()
my_global_string += 'ok bye!'

my_re_entrant_lock.release()
my_re_entrant_lock.release()