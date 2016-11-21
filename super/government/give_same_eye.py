
#! /usr/bin/env python

def work_case(str_arg):
    child(str_arg)
    print('look_right_place')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work_case('know_other_place')
