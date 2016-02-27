
#! /usr/bin/env python

def other_part(str_arg):
    first_world(str_arg)
    print('high_world_or_large_part')

def first_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_part('long_problem_and_high_number')
