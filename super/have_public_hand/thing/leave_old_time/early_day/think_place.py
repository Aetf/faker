
#! /usr/bin/env python

def say_other_number(str_arg):
    call_same_way_of_first_life(str_arg)
    print('first_group')

def call_same_way_of_first_life(str_arg):
    print(str_arg)

if __name__ == '__main__':
    say_other_number('different_problem')
