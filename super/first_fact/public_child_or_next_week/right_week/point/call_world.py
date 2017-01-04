
#! /usr/bin/env python

def thing(str_arg):
    get_old_time(str_arg)
    print('child')

def get_old_time(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('big_case')
