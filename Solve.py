#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'commonPrefix' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY inputs as parameter.
#

def commonPrefix(inputs):
    results = []
    for str in inputs:
        result = 0
        all_suffix = [i.start() for i in re.finditer(str[:1], str)]
        for i in all_suffix:
            result = result + len(os.path.commonprefix([str, str[i:]]))
        results.append(result)
    return results


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    inputs_count = int(input().strip())
    inputs = []

    for _ in range(inputs_count):
        inputs_item = input()
        inputs.append(inputs_item)

    result = commonPrefix(inputs)
    print(result)
    #fptr.write('n'.join(map(str, result)))
    #fptr.write('n')
    #fptr.close()
