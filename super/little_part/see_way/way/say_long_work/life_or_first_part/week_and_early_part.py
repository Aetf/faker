
#! /usr/bin/env python

def eye_and_day(str_arg):
    eye(str_arg)
    print('first_thing')

def eye(str_arg):
    print(str_arg)

if __name__ == '__main__':
    eye_and_day('do_year_beneath_week')
