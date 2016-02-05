
#! /usr/bin/env python

def part(str_arg):
    great_child(str_arg)
    print('new_group')

def great_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    part('child')
