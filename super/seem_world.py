
#! /usr/bin/env python

def important_world(str_arg):
    eye(str_arg)
    print('long_child')

def eye(str_arg):
    print(str_arg)

if __name__ == '__main__':
    important_world('child')
