
#! /usr/bin/env python

def old_child(str_arg):
    come_high_child(str_arg)
    print('different_way')

def come_high_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    old_child('few_case')
