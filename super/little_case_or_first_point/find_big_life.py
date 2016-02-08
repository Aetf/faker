
#! /usr/bin/env python

def early_world(str_arg):
    good_man(str_arg)
    print('point')

def good_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    early_world('bad_point_or_way')
