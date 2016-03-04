
#! /usr/bin/env python

def child_and_hand(str_arg):
    make_man_into_large_number(str_arg)
    print('child')

def make_man_into_large_number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child_and_hand('important_person')
