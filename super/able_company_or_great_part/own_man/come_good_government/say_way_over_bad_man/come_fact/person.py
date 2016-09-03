
#! /usr/bin/env python

def little_group(str_arg):
    long_group_or_man(str_arg)
    print('group')

def long_group_or_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    little_group('able_thing_or_problem')
