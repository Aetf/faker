
#! /usr/bin/env python

def early_world(str_arg):
    bad_child(str_arg)
    print('problem')

def bad_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    early_world('take_other_thing_under_public_thing')
