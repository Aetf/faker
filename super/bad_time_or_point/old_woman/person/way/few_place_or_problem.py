
#! /usr/bin/env python

def year(str_arg):
    group_or_big_time(str_arg)
    print('child')

def group_or_big_time(str_arg):
    print(str_arg)

if __name__ == '__main__':
    year('bad_year_and_year')
