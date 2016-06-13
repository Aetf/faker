
#! /usr/bin/env python

def different_work(str_arg):
    group(str_arg)
    print('public_thing')

def group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    different_work('early_way')
