
#! /usr/bin/env python

def child_and_world(str_arg):
    right_work(str_arg)
    print('thing')

def right_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child_and_world('call_government')
