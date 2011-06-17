#!/usr/bin/env python
# encoding: utf-8

'''
Author: Ken Graham
Copyright (c) 2011, Ken Graham

'''

import fileinput

filename = 'hyperpublic-challenge2input.txt'

# the i_th line of the input tells you which users the i_th user brought in
# this is stored in users[]

users = [list(row) for row in fileinput.input([filename])]
users = dict((i,users[i]) for i in range(len(users)))
num_users_added = [users[u].count('X') for u in users]

index_of_added_user = {}
for u in users:
    j=0
    index_of_added_user[u]=[]
    for n in users[u]:
        if (n == 'X'):
            index_of_added_user[u].append(j)
        j = j+1
  
def influence(x):
    if (num_users_added[x] == 0):
        return 0
    else:
        sum = num_users_added[x]
        for u in index_of_added_user[x]:
            sum = sum + influence(u)
        return sum
    
user_influence = []
for i in range(0,len(users)-1):
    user_influence.append(influence(i))
  
user_influence.sort(reverse=True)
print "%s%s%s" % (user_influence[0],user_influence[1],user_influence[2])
