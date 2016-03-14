
#! /usr/bin/env python

def first_world(str_arg):
    government(str_arg)
    print('other_government')

def government(str_arg):
    print(str_arg)

if __name__ == '__main__':
    first_world('life')
