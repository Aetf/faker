
#! /usr/bin/env python

def long_person(str_arg):
    fact(str_arg)
    print('child')

def fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    long_person('seem_big_man')
