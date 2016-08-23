
#! /usr/bin/env python

def life(str_arg):
    work(str_arg)
    print('world')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    life('use_case')
