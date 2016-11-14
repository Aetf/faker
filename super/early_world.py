
#! /usr/bin/env python

def new_case(str_arg):
    other_group_or_life(str_arg)
    print('child')

def other_group_or_life(str_arg):
    print(str_arg)

if __name__ == '__main__':
    new_case('good_man_or_old_number')
