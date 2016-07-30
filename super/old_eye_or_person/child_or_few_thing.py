
#! /usr/bin/env python

def little_part(str_arg):
    good_part(str_arg)
    print('come_place')

def good_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    little_part('world')
