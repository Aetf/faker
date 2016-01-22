
#! /usr/bin/env python

def be_early_life(str_arg):
    world(str_arg)
    print('other_case')

def world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    be_early_life('group')
