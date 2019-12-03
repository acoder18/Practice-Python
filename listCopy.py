#this script is tp learn about copy and Deepcopy

import copy

def listCopy():
    orig = [1,2,3,4]
    dup = orig
    print("print Orig ") + str(orig)
    orig.append("Hello")
    print("Print dup ") + str(dup)

listCopy()
