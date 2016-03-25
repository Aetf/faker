
#! /usr/bin/env python

def child(str_arg):
    long_man(str_arg)
    print('place')

def long_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('next_work')
