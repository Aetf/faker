
#! /usr/bin/env python

def other_thing_or_group(str_arg):
    first_part(str_arg)
    print('own_place_and_different_child')

def first_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_thing_or_group('old_problem_or_last_week')
