
#! /usr/bin/env python

def good_government(str_arg):
    government(str_arg)
    print('think_last_thing')

def government(str_arg):
    print(str_arg)

if __name__ == '__main__':
    good_government('bad_place')
