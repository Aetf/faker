
#! /usr/bin/env python

def work_or_case(str_arg):
    do_bad_problem_into_good_hand(str_arg)
    print('child')

def do_bad_problem_into_good_hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work_or_case('make_bad_place')
