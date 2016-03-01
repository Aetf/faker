
#! /usr/bin/env python

def call_long_time_by_time(str_arg):
    group(str_arg)
    print('important_problem')

def group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_long_time_by_time('big_world_and_work')
