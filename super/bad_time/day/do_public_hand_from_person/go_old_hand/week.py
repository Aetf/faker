
#! /usr/bin/env python

def different_time(str_arg):
    same_thing(str_arg)
    print('same_case_and_year')

def same_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    different_time('bad_point')
