
#! /usr/bin/env python

def first_case(str_arg):
    find_child(str_arg)
    print('long_hand')

def find_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    first_case('way')
