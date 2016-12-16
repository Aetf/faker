
#! /usr/bin/env python

def small_time(str_arg):
    part(str_arg)
    print('big_child')

def part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    small_time('tell_year')
