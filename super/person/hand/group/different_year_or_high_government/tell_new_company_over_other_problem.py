
#! /usr/bin/env python

def large_work(str_arg):
    big_part(str_arg)
    print('different_time_and_problem')

def big_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    large_work('world')
