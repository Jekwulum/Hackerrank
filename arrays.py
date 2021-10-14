import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    a = arr[::-1]
    a = numpy.array(a, float)
    return a

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
