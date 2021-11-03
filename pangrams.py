#!/bin/python3

import math
import os
import random
import re
import sys
# import string
#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(words):
    # remove special characters
    wordsList = " ".join(val.lower() for val in words if val.isalnum()).strip().split()
    # alphabets = list(string.ascii_lowercase)
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    myList = list(set(wordsList) & set(alphabets))
    
    if len(myList) == 26:
        return "pangram"
    else:
        return "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
