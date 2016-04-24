
#! /usr/bin/env python

def be_long_child(str_arg):
    long_group_and_fact(str_arg)
    print('eye')

def long_group_and_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    be_long_child('week')
