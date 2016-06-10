
#! /usr/bin/env python

def point(str_arg):
    early_way(str_arg)
    print('new_child')

def early_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    point('right_work')
