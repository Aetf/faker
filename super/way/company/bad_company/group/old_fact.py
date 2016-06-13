
#! /usr/bin/env python

def thing(str_arg):
    good_way(str_arg)
    print('work')

def good_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('first_group')
