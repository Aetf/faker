
#! /usr/bin/env python

def child_and_own_week(str_arg):
    child_or_early_work(str_arg)
    print('have_child')

def child_or_early_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child_and_own_week('call_long_time')
