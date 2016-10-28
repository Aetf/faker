
#! /usr/bin/env python

def company(str_arg):
    part(str_arg)
    print('try_new_thing_in_child')

def part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    company('week_and_big_thing')
