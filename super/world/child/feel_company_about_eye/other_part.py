
#! /usr/bin/env python

def high_eye(str_arg):
    try_own_part_at_place(str_arg)
    print('try_world')

def try_own_part_at_place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    high_eye('new_fact')
