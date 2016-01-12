
#! /usr/bin/env python

def big_work(str_arg):
    old_man(str_arg)
    print('man')

def old_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    big_work('point')
