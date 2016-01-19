
#! /usr/bin/env python

def try_person(str_arg):
    want_new_thing(str_arg)
    print('fact')

def want_new_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    try_person('bad_world')
