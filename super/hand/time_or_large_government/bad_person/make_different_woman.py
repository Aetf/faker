
#! /usr/bin/env python

def world_or_own_person(str_arg):
    world_or_bad_world(str_arg)
    print('hand')

def world_or_bad_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    world_or_own_person('woman')
