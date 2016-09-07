
#! /usr/bin/env python

def part(str_arg):
    man(str_arg)
    print('old_child')

def man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    part('high_point')
