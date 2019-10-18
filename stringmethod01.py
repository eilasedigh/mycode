#!/usr/bin/env python3

""" testing pylint"""
def main():
    """ thesting lylint"""
    lilstring = "Atlas3 Reasearch offers classes on Python coding"
    newlist = lilstring.split(" ") 
    print(newlist)

    myiplist = ["192", "168", "0", "12"]
    singleip = '.'.join(myiplist)
    print(singleip)

main()
