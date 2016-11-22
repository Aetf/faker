
#! /usr/bin/env python

def call_old_way(str_arg):
    call_thing_for_man(str_arg)
    print('young_part')

def call_thing_for_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_old_way('child_or_fact')
