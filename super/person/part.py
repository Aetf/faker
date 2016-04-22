
#! /usr/bin/env python

def try_right_work(str_arg):
    time_and_number(str_arg)
    print('call_child_to_child')

def time_and_number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    try_right_work('government')
