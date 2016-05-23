
#! /usr/bin/env python

def place_or_world(str_arg):
    see_problem(str_arg)
    print('child')

def see_problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    place_or_world('get_man')
