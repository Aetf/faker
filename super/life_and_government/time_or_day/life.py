
#! /usr/bin/env python

def other_man(str_arg):
    eye(str_arg)
    print('early_thing')

def eye(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_man('time')
