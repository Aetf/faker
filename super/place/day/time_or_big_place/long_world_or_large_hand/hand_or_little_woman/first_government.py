
#! /usr/bin/env python

def have_place(str_arg):
    work(str_arg)
    print('early_point_or_child')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    have_place('world')
