
#! /usr/bin/env python

def small_thing_or_work(str_arg):
    point_and_work(str_arg)
    print('come_work')

def point_and_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    small_thing_or_work('part')
