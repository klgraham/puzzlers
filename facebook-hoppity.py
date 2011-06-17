#!/usr/bin/env python2.5
# encoding: utf-8

''' 
Author: Ken Graham
Copyright (c) 2011, Ken Graham
All rights reserved.
'''

# open file and read number
infile = open(r'hoppity_input.txt','r')
iterationString = infile.read()

# strip newline, then strip padding spaces, then cast to integer
n = int((iterationString.strip('\n')).strip(' '))

# dictionary of possible results
output = {
    (True,False): 'Hoppity',
    (False,True): 'Hophop',
    (True,True): 'Hop'
}
 
for x in range(1,n):
    # evenly divisible by three or five?
    multipleOfThree = bool(x % 3 == 0)
    multipleOfFive = bool(x % 5 == 0)
  
    result = output.get((multipleOfThree,multipleOfFive))
    if bool(result):
        print(result)
