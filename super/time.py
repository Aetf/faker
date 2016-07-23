
#! /usr/bin/env python

def child_or_big_point(str_arg):
    work(str_arg)
    print('world')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child_or_big_point('company')
