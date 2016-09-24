
#! /usr/bin/env python

def child(str_arg):
    part(str_arg)
    print('new_week_and_problem')

def part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('different_part_or_child')
