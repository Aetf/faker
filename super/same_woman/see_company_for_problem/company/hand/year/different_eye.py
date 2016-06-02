
#! /usr/bin/env python

def old_part(str_arg):
    take_part(str_arg)
    print('call_case')

def take_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    old_part('first_eye')
