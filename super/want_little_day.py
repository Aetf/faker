
#! /usr/bin/env python

def man(str_arg):
    case(str_arg)
    print('own_child')

def case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man('day')
