
#! /usr/bin/env python

def part(str_arg):
    important_thing(str_arg)
    print('bad_child')

def important_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    part('young_work')
