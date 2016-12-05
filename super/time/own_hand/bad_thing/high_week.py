
#! /usr/bin/env python

def new_point_or_world(str_arg):
    early_child(str_arg)
    print('world')

def early_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    new_point_or_world('say_public_place')
