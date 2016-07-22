
#! /usr/bin/env python

def different_work_and_child(str_arg):
    small_world(str_arg)
    print('problem')

def small_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    different_work_and_child('old_work_and_group')
