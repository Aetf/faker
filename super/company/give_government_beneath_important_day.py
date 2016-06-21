
#! /usr/bin/env python

def number_or_bad_thing(str_arg):
    long_number_and_big_problem(str_arg)
    print('great_number')

def long_number_and_big_problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    number_or_bad_thing('say_own_man')
