
#! /usr/bin/env python

def early_way(str_arg):
    thing_or_child(str_arg)
    print('early_world_and_big_child')

def thing_or_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    early_way('do_place')
