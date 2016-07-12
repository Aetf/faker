
#! /usr/bin/env python

def bad_group(str_arg):
    bad_man(str_arg)
    print('first_part')

def bad_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_group('world_or_large_part')
