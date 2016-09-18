
#! /usr/bin/env python

def new_government(str_arg):
    use_bad_case(str_arg)
    print('government')

def use_bad_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    new_government('fact')
