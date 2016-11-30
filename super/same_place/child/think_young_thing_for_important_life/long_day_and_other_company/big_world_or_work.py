
#! /usr/bin/env python

def bad_case(str_arg):
    little_day_or_new_number(str_arg)
    print('week_or_day')

def little_day_or_new_number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_case('man')
