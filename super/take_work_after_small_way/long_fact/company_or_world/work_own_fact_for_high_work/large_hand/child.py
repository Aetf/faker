
#! /usr/bin/env python

def work(str_arg):
    last_life(str_arg)
    print('child')

def last_life(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work('part_and_world')
