
#! /usr/bin/env python

def own_time(str_arg):
    old_way(str_arg)
    print('important_way')

def old_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    own_time('eye')
