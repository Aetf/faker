
#! /usr/bin/env python

def public_thing(str_arg):
    way(str_arg)
    print('great_child')

def way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    public_thing('big_part_and_same_fact')
