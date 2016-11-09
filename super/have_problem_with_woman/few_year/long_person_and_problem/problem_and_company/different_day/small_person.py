
#! /usr/bin/env python

def company(str_arg):
    part_or_man(str_arg)
    print('new_man')

def part_or_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    company('hand')
