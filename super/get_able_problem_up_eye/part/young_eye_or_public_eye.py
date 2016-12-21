
#! /usr/bin/env python

def different_world(str_arg):
    leave_little_world(str_arg)
    print('fact')

def leave_little_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    different_world('little_man')
