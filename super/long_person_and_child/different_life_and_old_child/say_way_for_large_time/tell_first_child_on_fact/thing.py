
#! /usr/bin/env python

def early_part(str_arg):
    eye(str_arg)
    print('child_or_world')

def eye(str_arg):
    print(str_arg)

if __name__ == '__main__':
    early_part('last_year')
