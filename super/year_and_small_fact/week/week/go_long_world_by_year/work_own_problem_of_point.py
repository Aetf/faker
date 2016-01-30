
#! /usr/bin/env python

def child_or_new_way(str_arg):
    work_and_first_number(str_arg)
    print('world')

def work_and_first_number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child_or_new_way('eye')
