
#! /usr/bin/env python

def different_point(str_arg):
    early_child_or_part(str_arg)
    print('part')

def early_child_or_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    different_point('first_child')
