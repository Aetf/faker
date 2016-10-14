
#! /usr/bin/env python

def own_group(str_arg):
    own_man(str_arg)
    print('important_fact')

def own_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    own_group('next_day')
