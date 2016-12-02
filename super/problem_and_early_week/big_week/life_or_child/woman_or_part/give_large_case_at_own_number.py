
#! /usr/bin/env python

def child(str_arg):
    child(str_arg)
    print('leave_government')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('early_child_and_part')
