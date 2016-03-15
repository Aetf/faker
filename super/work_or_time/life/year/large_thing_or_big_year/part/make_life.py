
#! /usr/bin/env python

def big_thing(str_arg):
    other_problem_and_place(str_arg)
    print('case')

def other_problem_and_place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    big_thing('long_thing')
