
#! /usr/bin/env python

def work(str_arg):
    part_or_life(str_arg)
    print('work')

def part_or_life(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work('child')
