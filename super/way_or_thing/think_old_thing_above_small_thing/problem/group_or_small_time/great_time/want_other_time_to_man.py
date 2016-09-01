
#! /usr/bin/env python

def man(str_arg):
    group(str_arg)
    print('own_time_or_other_case')

def group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man('year')
