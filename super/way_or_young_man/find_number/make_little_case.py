
#! /usr/bin/env python

def call_early_point_at_own_number(str_arg):
    go_same_day(str_arg)
    print('part')

def go_same_day(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_early_point_at_own_number('day')
