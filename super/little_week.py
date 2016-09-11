
#! /usr/bin/env python

def point(str_arg):
    bad_way(str_arg)
    print('group')

def bad_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    point('high_way')
