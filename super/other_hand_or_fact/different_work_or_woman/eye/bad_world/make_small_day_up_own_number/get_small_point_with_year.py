
#! /usr/bin/env python

def problem(str_arg):
    big_world(str_arg)
    print('old_child')

def big_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    problem('place')
