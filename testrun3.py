"""Creating Numpy arrays"""

import numpy as np

def get_max_index(a):
    """Return the index of the maximum value in the given 1D array"""
    return a.argmax()

def test_run():
    # List to 1D array
    # print( np.array([2,3,4]))

    # List of tuples to 2D array
    # print(np.array([(2,3,4), (5,6,7)]))

    a = np.array([9, 6, 2, 3, 12, 14, 7, 10], dtype=np.int32)  # 32-bit integer array
    print("Array:", a)

    # Find the maximun and its index in array
    print("Maximun value:", a.max())
    print("Index of max.:", get_max_index(a))

if __name__ == "__main__":
    test_run()