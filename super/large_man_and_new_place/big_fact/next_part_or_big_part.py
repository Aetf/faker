
#! /usr/bin/env python

def man(str_arg):
    place_or_child(str_arg)
    print('man')

def place_or_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man('point')
