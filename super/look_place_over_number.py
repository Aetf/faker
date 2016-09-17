
#! /usr/bin/env python

def number(str_arg):
    other_way(str_arg)
    print('next_case')

def other_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    number('child')
