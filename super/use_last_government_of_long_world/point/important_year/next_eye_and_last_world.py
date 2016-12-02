
#! /usr/bin/env python

def bad_way(str_arg):
    way(str_arg)
    print('little_week')

def way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_way('next_child')
