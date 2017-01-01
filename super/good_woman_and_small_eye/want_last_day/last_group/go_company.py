
#! /usr/bin/env python

def right_work(str_arg):
    other_work(str_arg)
    print('world')

def other_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    right_work('do_way_with_public_life')
