
#! /usr/bin/env python

def bad_thing(str_arg):
    important_time(str_arg)
    print('big_thing')

def important_time(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_thing('little_day')
