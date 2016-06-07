
#! /usr/bin/env python

def work_and_hand(str_arg):
    small_hand(str_arg)
    print('own_time')

def small_hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work_and_hand('own_week')
