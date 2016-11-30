
#! /usr/bin/env python

def public_part_or_number(str_arg):
    fact(str_arg)
    print('child')

def fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    public_part_or_number('use_life_for_woman')
