
#! /usr/bin/env python

def government(str_arg):
    case(str_arg)
    print('government_or_world')

def case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    government('world')
