
#! /usr/bin/env python

def want_bad_man(str_arg):
    place(str_arg)
    print('different_man')

def place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    want_bad_man('small_man')
