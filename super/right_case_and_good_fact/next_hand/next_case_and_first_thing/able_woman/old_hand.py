
#! /usr/bin/env python

def other_time_or_work(str_arg):
    leave_thing(str_arg)
    print('work')

def leave_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_time_or_work('child')
