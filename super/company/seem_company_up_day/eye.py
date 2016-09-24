
#! /usr/bin/env python

def small_world(str_arg):
    new_thing(str_arg)
    print('small_eye')

def new_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    small_world('good_place_or_important_point')
