
#! /usr/bin/env python

def fact(str_arg):
    call_different_child(str_arg)
    print('woman')

def call_different_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    fact('bad_time')
