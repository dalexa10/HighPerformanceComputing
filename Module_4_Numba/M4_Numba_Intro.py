
# ---- Intro ----
# To recall: numba allows to speed-up existing Python code without any language extension
# It translates Python code to optimized machine code using LLVM compiler

# ---- Setting Up ------
# Locally: pip install numba in your environment
# Collab: !pip install numba

# ---- Code Example -----
from numba import jit
import time

# Conventional code
def factorial(n):
    fact = 1
    for x in range(1, n+1):
        fact = fact * x
    return fact
start1 = time.time()
factorial(100000)
end1 = time.time()
print('Time for conventional code is {} seconds'.format(end1 - start1))

# Using numba
# Recall to test this part, numpy must be version 1.20 or lower (type in your conda environment
# conda install -c conda-forge numpy=1.20    to downgrade it)
@jit
def factorial_numba(n):
    fact = 1
    for x in range(1, n+1):
        fact = fact * x
    return fact
start2 = time.time()
factorial_numba(100000)
end2 = time.time()
print('Time for numba code is {} seconds'.format(end2 - start2))
