
#! /usr/bin/env python

def take_long_time_in_important_case(str_arg):
    public_point(str_arg)
    print('different_work_and_early_place')

def public_point(str_arg):
    print(str_arg)

if __name__ == '__main__':
    take_long_time_in_important_case('go_child')
