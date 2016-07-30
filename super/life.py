
#! /usr/bin/env python

def man(str_arg):
    eye(str_arg)
    print('do_part')

def eye(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man('large_year_and_long_time')
