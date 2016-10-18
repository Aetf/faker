
#! /usr/bin/env python

def same_thing(str_arg):
    person(str_arg)
    print('woman')

def person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    same_thing('do_time')
