
#! /usr/bin/env python

def point(str_arg):
    try_early_child(str_arg)
    print('go_man')

def try_early_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    point('large_day')
