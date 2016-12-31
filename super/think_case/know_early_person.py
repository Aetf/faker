
#! /usr/bin/env python

def work(str_arg):
    same_way(str_arg)
    print('bad_world')

def same_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work('point')
