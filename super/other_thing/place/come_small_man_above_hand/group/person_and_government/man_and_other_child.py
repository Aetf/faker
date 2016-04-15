
#! /usr/bin/env python

def way(str_arg):
    first_work_and_last_group(str_arg)
    print('child')

def first_work_and_last_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    way('large_part')
