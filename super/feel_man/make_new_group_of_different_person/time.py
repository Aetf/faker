
#! /usr/bin/env python

def large_thing(str_arg):
    good_woman(str_arg)
    print('other_world')

def good_woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    large_thing('person')
