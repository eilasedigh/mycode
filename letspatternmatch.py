#!/usr/bin/env python3

import os,fnmatch
def find_all(pattern,path):
    result=[]
    for root, dirs, files in os.walk(path):
        for name in files:
         if fnmatch.fnmatch(name, pattern):
            result.append(os.path.join(root, name))
    return result

lookfor = input("What pattern am I looking for? ")
lookwhere = input("What is the path in which I should search? ")

a=find_all(lookfor, lookwhere)


for x in a:
    print(x)
