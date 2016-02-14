
#! /usr/bin/env python

def new_week_or_same_problem(str_arg):
    call_next_way_with_world(str_arg)
    print('week')

def call_next_way_with_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    new_week_or_same_problem('place_or_bad_person')
