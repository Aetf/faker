
#! /usr/bin/env python

def call_own_part_at_different_child(str_arg):
    go_week(str_arg)
    print('big_man')

def go_week(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_own_part_at_different_child('time_and_time')
