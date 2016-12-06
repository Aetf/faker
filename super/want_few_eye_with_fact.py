
#! /usr/bin/env python

def good_child(str_arg):
    come_group(str_arg)
    print('young_child')

def come_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    good_child('high_life')
