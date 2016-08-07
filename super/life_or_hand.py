
#! /usr/bin/env python

def other_life(str_arg):
    public_way(str_arg)
    print('bad_man')

def public_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_life('call_group_into_same_thing')
