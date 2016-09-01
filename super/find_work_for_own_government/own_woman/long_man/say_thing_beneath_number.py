
#! /usr/bin/env python

def see_other_child(str_arg):
    big_world(str_arg)
    print('take_big_group')

def big_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    see_other_child('number')
