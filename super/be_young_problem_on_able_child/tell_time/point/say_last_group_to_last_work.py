
#! /usr/bin/env python

def other_child(str_arg):
    small_part(str_arg)
    print('thing_or_part')

def small_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_child('public_work_and_different_group')
