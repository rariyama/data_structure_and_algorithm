#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    n = len(a)
    cnt = 0
    for _ in range(n-1):
        for j in reversed(range(1, n)):
            if a[j] < a[j-1]:
                temp = a[j]
                a[j] = a[j-1]
                a[j-1] = temp
                cnt += 1
    print('Array is sorted in {} swaps.'.format(cnt))
    print('First Element: {}'.format(a[0]))
    print('Last Element: {}'.format(a[-1]))
        
        
        

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
