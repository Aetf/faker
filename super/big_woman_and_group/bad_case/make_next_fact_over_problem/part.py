
#! /usr/bin/env python

def long_man(str_arg):
    child(str_arg)
    print('man')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    long_man('eye_or_public_place')
