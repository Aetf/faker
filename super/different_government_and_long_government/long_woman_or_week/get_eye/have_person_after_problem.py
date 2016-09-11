
#! /usr/bin/env python

def tell_thing_over_place(str_arg):
    call_first_case(str_arg)
    print('other_person_or_problem')

def call_first_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    tell_thing_over_place('eye')
