
#! /usr/bin/env python

def work_long_part(str_arg):
    world(str_arg)
    print('little_world')

def world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work_long_part('way')
