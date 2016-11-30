
#! /usr/bin/env python

def bad_group(str_arg):
    work(str_arg)
    print('way')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_group('fact')
