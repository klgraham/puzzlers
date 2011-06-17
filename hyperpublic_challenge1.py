#!/usr/bin/env python
# encoding: utf-8

'''
Author: Ken Graham
Copyright (c) 2011, Ken Graham

'''

# hyperpublic_challenge1.py

# running on Python 2.7.1

input = open('hyperpublic-challenge2input.txt','r')

# the i_th line of the file tells you which users the i_th user brought in
users = {}
num_users_added = {}
i=0
for row in input:
  # user[i] tells you which users were added by user i
  users[i] = list(row)
  # users_added_by[i] tells who how many users were added by user i
  num_users_added[i] = row.count('X')
  i = i+1
  
index_of_adds = {}
for u in users:
  j=0
  index_of_adds[u]=[]
  for n in users[u]:
    if n=='X':
      index_of_adds[u].append(j)
    j = j+1
  
def influence(x):
  if num_users_added[x] == 0:
    return 0
  else:
    sum = num_users_added[x]
    for u in index_of_adds[x]:
      sum = sum + influence(u)
    return sum
    
user_influence = []
for i in range(0,len(users)-1):
  user_influence.append(influence(i))
  
user_influence.sort()
user_influence.reverse()
print "%s%s%s" % (user_influence[0],user_influence[1],user_influence[2])
