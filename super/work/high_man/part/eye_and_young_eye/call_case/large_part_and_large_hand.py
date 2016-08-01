
#! /usr/bin/env python

def try_public_thing_on_problem(str_arg):
    look_long_time(str_arg)
    print('public_fact')

def look_long_time(str_arg):
    print(str_arg)

if __name__ == '__main__':
    try_public_thing_on_problem('right_number')
