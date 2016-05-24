
#! /usr/bin/env python

def world(str_arg):
    world_or_other_thing(str_arg)
    print('same_way_or_same_place')

def world_or_other_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    world('new_work_or_own_year')
