
#! /usr/bin/env python

def big_world(str_arg):
    child(str_arg)
    print('life')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    big_world('life')
