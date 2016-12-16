
#! /usr/bin/env python

def problem_or_child(str_arg):
    point_or_thing(str_arg)
    print('bad_thing')

def point_or_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    problem_or_child('problem_and_last_day')
