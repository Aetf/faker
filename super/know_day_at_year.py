
#! /usr/bin/env python

def tell_world(str_arg):
    work(str_arg)
    print('big_world')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    tell_world('world_and_group')
