
#! /usr/bin/env python

def bad_place(str_arg):
    big_man(str_arg)
    print('eye_or_high_place')

def big_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_place('other_eye')
