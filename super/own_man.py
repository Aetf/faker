
#! /usr/bin/env python

def world_and_child(str_arg):
    life_or_point(str_arg)
    print('world')

def life_or_point(str_arg):
    print(str_arg)

if __name__ == '__main__':
    world_and_child('problem_and_last_child')
