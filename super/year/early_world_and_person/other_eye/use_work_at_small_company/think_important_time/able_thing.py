
#! /usr/bin/env python

def other_world(str_arg):
    life(str_arg)
    print('do_work')

def life(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_world('different_problem')
