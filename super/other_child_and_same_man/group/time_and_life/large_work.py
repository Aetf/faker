
#! /usr/bin/env python

def life(str_arg):
    make_child_over_same_group(str_arg)
    print('big_work')

def make_child_over_same_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    life('fact')
