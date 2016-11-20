
#! /usr/bin/env python

def get_number(str_arg):
    public_child(str_arg)
    print('eye')

def public_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    get_number('old_part_and_thing')
