
#! /usr/bin/env python

def new_thing(str_arg):
    early_point(str_arg)
    print('next_problem')

def early_point(str_arg):
    print(str_arg)

if __name__ == '__main__':
    new_thing('small_number')
