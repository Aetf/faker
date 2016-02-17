
#! /usr/bin/env python

def bad_work(str_arg):
    woman(str_arg)
    print('small_point')

def woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_work('week')
