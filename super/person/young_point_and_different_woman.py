
#! /usr/bin/env python

def place(str_arg):
    own_work_or_same_group(str_arg)
    print('go_child')

def own_work_or_same_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    place('life')
