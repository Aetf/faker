
#! /usr/bin/env python

def do_other_part(str_arg):
    do_case(str_arg)
    print('new_work')

def do_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    do_other_part('do_case_from_early_fact')
