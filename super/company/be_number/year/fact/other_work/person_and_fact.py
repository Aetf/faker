
#! /usr/bin/env python

def different_case(str_arg):
    important_case(str_arg)
    print('see_right_day')

def important_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    different_case('year_and_fact')
