
#! /usr/bin/env python

def other_world(str_arg):
    point(str_arg)
    print('small_point')

def point(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_world('own_time')
