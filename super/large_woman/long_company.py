
#! /usr/bin/env python

def own_work(str_arg):
    bad_point(str_arg)
    print('new_fact')

def bad_point(str_arg):
    print(str_arg)

if __name__ == '__main__':
    own_work('small_time')
