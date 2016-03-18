
#! /usr/bin/env python

def man_and_point(str_arg):
    world(str_arg)
    print('leave_point')

def world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man_and_point('number_or_year')
