
#! /usr/bin/env python

def long_work_or_part(str_arg):
    thing(str_arg)
    print('way')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    long_work_or_part('way')
