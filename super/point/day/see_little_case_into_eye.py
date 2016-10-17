
#! /usr/bin/env python

def call_part(str_arg):
    important_part(str_arg)
    print('feel_long_work')

def important_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_part('day_or_case')
