
#! /usr/bin/env python

def think_bad_man(str_arg):
    own_place(str_arg)
    print('public_way')

def own_place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    think_bad_man('thing_or_way')
