
#! /usr/bin/env python

def good_place(str_arg):
    long_child(str_arg)
    print('last_eye')

def long_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    good_place('go_number_in_year')
