
#! /usr/bin/env python

def other_thing(str_arg):
    early_point(str_arg)
    print('world')

def early_point(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_thing('early_point')
