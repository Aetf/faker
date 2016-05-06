
#! /usr/bin/env python

def different_man(str_arg):
    old_child(str_arg)
    print('make_big_way')

def old_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    different_man('person')
