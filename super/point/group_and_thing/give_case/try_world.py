
#! /usr/bin/env python

def point_or_fact(str_arg):
    way(str_arg)
    print('call_way')

def way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    point_or_fact('child')
