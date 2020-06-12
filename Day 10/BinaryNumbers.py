#!/bin/python3

import math
import os
import random
import re
import sys


def DecimalToBinary(n):
    binary = ""
    if n == 0:
        return "0"
    else:
        while n > 1:
            binary = binary + str(n%2)
            n = int(n/2)
        binary = binary + "1"
    return binary[::-1]

def NumberOfOnes(binary):
    n = len(binary)+1
    cont = True
    while cont:
        test = n*"1"
        if test in binary:
            cont = False
        else:
            n = n-1
    return n

if __name__ == '__main__':
    n = int(input())
    a = DecimalToBinary(n)
    print(NumberOfOnes(a))
