
#! /usr/bin/env python

def man(str_arg):
    next_man(str_arg)
    print('call_other_case')

def next_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man('young_number')
