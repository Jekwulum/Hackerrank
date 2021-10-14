#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def check_if_camelCase(string):
    """
    This checks if a string is camelCase
    """
    if string[0] == string[0].lower():
        return True
    else:
        return False

def camelcase(string):
    # Write your code here
    count = 1
    if check_if_camelCase(string):
        for i in string:
            if i == i.upper():
                count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
