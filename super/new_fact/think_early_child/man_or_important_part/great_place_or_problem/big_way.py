
#! /usr/bin/env python

def world_or_time(str_arg):
    place_and_year(str_arg)
    print('world')

def place_and_year(str_arg):
    print(str_arg)

if __name__ == '__main__':
    world_or_time('year')
