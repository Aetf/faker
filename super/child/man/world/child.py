
#! /usr/bin/env python

def call_part_under_first_child(str_arg):
    tell_few_thing(str_arg)
    print('use_old_case')

def tell_few_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_part_under_first_child('first_person')
