
#! /usr/bin/env python

def eye_or_man(str_arg):
    long_way(str_arg)
    print('right_hand')

def long_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    eye_or_man('point')
