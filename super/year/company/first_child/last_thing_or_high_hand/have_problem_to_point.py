
#! /usr/bin/env python

def own_group(str_arg):
    man(str_arg)
    print('want_man')

def man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    own_group('group_or_fact')
