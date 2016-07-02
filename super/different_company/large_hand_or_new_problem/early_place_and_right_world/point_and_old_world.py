
#! /usr/bin/env python

def man(str_arg):
    long_point_or_hand(str_arg)
    print('long_number')

def long_point_or_hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man('time')
