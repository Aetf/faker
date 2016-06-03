
#! /usr/bin/env python

def part(str_arg):
    different_group(str_arg)
    print('own_child')

def different_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    part('case')
