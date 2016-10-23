
#! /usr/bin/env python

def group(str_arg):
    long_child(str_arg)
    print('group')

def long_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    group('fact_and_early_group')
