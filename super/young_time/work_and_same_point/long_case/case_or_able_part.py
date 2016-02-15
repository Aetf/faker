
#! /usr/bin/env python

def old_thing(str_arg):
    high_work(str_arg)
    print('other_case')

def high_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    old_thing('week_or_own_point')
