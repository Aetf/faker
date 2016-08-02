
#! /usr/bin/env python

def case(str_arg):
    child(str_arg)
    print('few_child')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    case('little_week')
