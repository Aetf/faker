
#! /usr/bin/env python

def child(str_arg):
    number(str_arg)
    print('first_case')

def number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('number')
