
#! /usr/bin/env python

def long_person_and_long_world(str_arg):
    world(str_arg)
    print('different_group')

def world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    long_person_and_long_world('large_point')
