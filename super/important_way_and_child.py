
#! /usr/bin/env python

def eye(str_arg):
    way(str_arg)
    print('own_child')

def way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    eye('public_man')
