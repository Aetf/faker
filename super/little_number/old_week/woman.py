
#! /usr/bin/env python

def woman(str_arg):
    tell_world(str_arg)
    print('world')

def tell_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    woman('year')
