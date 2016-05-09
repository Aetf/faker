
#! /usr/bin/env python

def world_and_bad_way(str_arg):
    large_person(str_arg)
    print('bad_thing')

def large_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    world_and_bad_way('first_place_or_part')
