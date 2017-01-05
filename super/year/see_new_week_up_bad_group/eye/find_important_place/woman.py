
#! /usr/bin/env python

def good_child(str_arg):
    thing(str_arg)
    print('fact')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    good_child('small_group_and_part')
