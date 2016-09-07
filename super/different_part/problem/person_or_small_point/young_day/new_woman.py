
#! /usr/bin/env python

def few_time(str_arg):
    bad_thing(str_arg)
    print('public_case')

def bad_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    few_time('find_next_number_with_world')
