
#! /usr/bin/env python

def year_and_other_world(str_arg):
    go_time(str_arg)
    print('child')

def go_time(str_arg):
    print(str_arg)

if __name__ == '__main__':
    year_and_other_world('point_or_case')
