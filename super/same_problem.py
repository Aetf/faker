
#! /usr/bin/env python

def point_and_way(str_arg):
    work(str_arg)
    print('world')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    point_and_way('fact')
