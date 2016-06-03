
#! /usr/bin/env python

def child(str_arg):
    own_man_or_bad_place(str_arg)
    print('own_way')

def own_man_or_bad_place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('case')
