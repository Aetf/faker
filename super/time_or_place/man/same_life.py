
#! /usr/bin/env python

def thing(str_arg):
    fact(str_arg)
    print('child')

def fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('eye')
