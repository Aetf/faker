
#! /usr/bin/env python

def use_important_fact_from_long_time(str_arg):
    first_thing(str_arg)
    print('fact')

def first_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    use_important_fact_from_long_time('little_case')
