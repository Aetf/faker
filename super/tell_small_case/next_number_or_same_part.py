
#! /usr/bin/env python

def next_week(str_arg):
    own_year_or_day(str_arg)
    print('week')

def own_year_or_day(str_arg):
    print(str_arg)

if __name__ == '__main__':
    next_week('old_case')
