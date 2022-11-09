import numpy as np
arr= np.arange(8)
arr2 = np.array([2,3,4,5], dtype=np.int8)
print(arr, '\n{}'.format(arr2))

arr3, step= np.linspace(-6,21,60, endpoint=False, retstep=True)
print(step)