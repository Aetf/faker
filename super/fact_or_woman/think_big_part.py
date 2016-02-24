
#! /usr/bin/env python

def other_man(str_arg):
    point(str_arg)
    print('next_time')

def point(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_man('part')
