
#! /usr/bin/env python

def woman_or_work(str_arg):
    woman(str_arg)
    print('part_or_place')

def woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    woman_or_work('right_day')
