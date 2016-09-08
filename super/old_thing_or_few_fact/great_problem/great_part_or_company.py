
#! /usr/bin/env python

def call_fact_in_little_thing(str_arg):
    small_number(str_arg)
    print('long_problem')

def small_number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_fact_in_little_thing('time')
