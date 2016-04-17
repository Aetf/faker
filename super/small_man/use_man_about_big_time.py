
#! /usr/bin/env python

def little_woman(str_arg):
    government(str_arg)
    print('government')

def government(str_arg):
    print(str_arg)

if __name__ == '__main__':
    little_woman('able_child')
