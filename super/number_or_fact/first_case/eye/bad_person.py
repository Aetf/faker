
#! /usr/bin/env python

def bad_work(str_arg):
    point(str_arg)
    print('part')

def point(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_work('world')
