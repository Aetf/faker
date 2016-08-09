
#! /usr/bin/env python

def point(str_arg):
    old_part_and_work(str_arg)
    print('thing')

def old_part_and_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    point('child')
