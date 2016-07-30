
#! /usr/bin/env python

def leave_life(str_arg):
    bad_part_or_way(str_arg)
    print('important_part')

def bad_part_or_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    leave_life('week')
