
#! /usr/bin/env python

def leave_life(str_arg):
    life(str_arg)
    print('young_thing')

def life(str_arg):
    print(str_arg)

if __name__ == '__main__':
    leave_life('first_problem')
