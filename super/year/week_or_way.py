
#! /usr/bin/env python

def work(str_arg):
    world(str_arg)
    print('small_man')

def world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work('world')
