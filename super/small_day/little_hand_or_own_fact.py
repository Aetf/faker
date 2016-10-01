
#! /usr/bin/env python

def eye(str_arg):
    hand(str_arg)
    print('own_world')

def hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    eye('different_company')
