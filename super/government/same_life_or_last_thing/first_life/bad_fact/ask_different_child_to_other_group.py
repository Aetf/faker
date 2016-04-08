
#! /usr/bin/env python

def first_hand(str_arg):
    right_work(str_arg)
    print('new_number')

def right_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    first_hand('thing')
