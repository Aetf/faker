
#! /usr/bin/env python

def leave_different_time(str_arg):
    government(str_arg)
    print('government')

def government(str_arg):
    print(str_arg)

if __name__ == '__main__':
    leave_different_time('bad_time_or_old_day')
