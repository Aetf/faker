
#! /usr/bin/env python

def same_way(str_arg):
    child(str_arg)
    print('first_way')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    same_way('day')
