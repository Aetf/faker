
#! /usr/bin/env python

def number_or_group(str_arg):
    child_or_group(str_arg)
    print('time')

def child_or_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    number_or_group('new_man')
