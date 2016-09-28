
#! /usr/bin/env python

def public_government(str_arg):
    fact(str_arg)
    print('world_and_last_fact')

def fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    public_government('hand')
