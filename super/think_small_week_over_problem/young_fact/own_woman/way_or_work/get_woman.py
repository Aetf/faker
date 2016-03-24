
#! /usr/bin/env python

def other_child(str_arg):
    tell_old_child(str_arg)
    print('different_number')

def tell_old_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_child('point_or_able_way')
