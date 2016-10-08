
#! /usr/bin/env python

def first_group(str_arg):
    child(str_arg)
    print('old_place')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    first_group('hand')
