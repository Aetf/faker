
#! /usr/bin/env python

def case(str_arg):
    long_child(str_arg)
    print('world')

def long_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    case('way')
