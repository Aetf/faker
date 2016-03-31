
#! /usr/bin/env python

def own_child_or_point(str_arg):
    long_way(str_arg)
    print('other_day')

def long_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    own_child_or_point('work')
