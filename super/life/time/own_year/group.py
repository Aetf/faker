
#! /usr/bin/env python

def want_child_with_world(str_arg):
    new_thing(str_arg)
    print('part')

def new_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    want_child_with_world('life')
