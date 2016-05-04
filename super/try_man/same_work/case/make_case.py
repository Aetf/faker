
#! /usr/bin/env python

def child_and_next_thing(str_arg):
    come_bad_world(str_arg)
    print('young_child')

def come_bad_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child_and_next_thing('person')
