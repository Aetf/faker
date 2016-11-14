
#! /usr/bin/env python

def different_world_or_point(str_arg):
    point_and_part(str_arg)
    print('child')

def point_and_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    different_world_or_point('high_place_and_part')
