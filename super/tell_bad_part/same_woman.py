
#! /usr/bin/env python

def child_and_old_case(str_arg):
    child(str_arg)
    print('time')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child_and_old_case('next_person')
