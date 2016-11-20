
#! /usr/bin/env python

def bad_man(str_arg):
    work(str_arg)
    print('new_world_or_own_problem')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_man('fact')
