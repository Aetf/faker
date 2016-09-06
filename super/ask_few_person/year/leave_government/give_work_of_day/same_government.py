
#! /usr/bin/env python

def call_problem_in_right_place(str_arg):
    year(str_arg)
    print('week')

def year(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_problem_in_right_place('other_thing')
