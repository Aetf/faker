
#! /usr/bin/env python

def large_child(str_arg):
    long_fact(str_arg)
    print('great_thing')

def long_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    large_child('first_child')
