
#! /usr/bin/env python

def case(str_arg):
    eye(str_arg)
    print('call_world')

def eye(str_arg):
    print(str_arg)

if __name__ == '__main__':
    case('new_part')
