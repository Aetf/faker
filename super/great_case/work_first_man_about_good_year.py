
#! /usr/bin/env python

def right_place(str_arg):
    look_early_child(str_arg)
    print('case')

def look_early_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    right_place('last_government')
