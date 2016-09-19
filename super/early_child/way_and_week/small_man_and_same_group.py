
#! /usr/bin/env python

def little_point(str_arg):
    way_or_way(str_arg)
    print('child')

def way_or_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    little_point('bad_company')
