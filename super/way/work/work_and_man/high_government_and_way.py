
#! /usr/bin/env python

def call_right_place_beneath_big_case(str_arg):
    call_bad_place_for_different_person(str_arg)
    print('woman')

def call_bad_place_for_different_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_right_place_beneath_big_case('try_life')
