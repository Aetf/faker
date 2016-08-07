
#! /usr/bin/env python

def think_same_thing(str_arg):
    long_work(str_arg)
    print('way')

def long_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    think_same_thing('way')
