
#! /usr/bin/env python

def important_point(str_arg):
    high_point(str_arg)
    print('different_number')

def high_point(str_arg):
    print(str_arg)

if __name__ == '__main__':
    important_point('number')
