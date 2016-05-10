
#! /usr/bin/env python

def long_man_and_first_case(str_arg):
    high_part(str_arg)
    print('child')

def high_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    long_man_and_first_case('find_hand_on_high_hand')
