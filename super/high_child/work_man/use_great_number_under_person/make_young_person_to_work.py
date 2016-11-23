
#! /usr/bin/env python

def first_hand(str_arg):
    tell_other_child(str_arg)
    print('government')

def tell_other_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    first_hand('good_government')
