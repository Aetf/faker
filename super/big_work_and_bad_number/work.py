
#! /usr/bin/env python

def call_able_group(str_arg):
    able_world(str_arg)
    print('first_way')

def able_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_able_group('different_fact')
