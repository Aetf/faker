
#! /usr/bin/env python

def child(str_arg):
    fact(str_arg)
    print('life')

def fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('small_child')
