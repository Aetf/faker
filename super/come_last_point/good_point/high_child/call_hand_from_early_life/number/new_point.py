
#! /usr/bin/env python

def place_or_company(str_arg):
    government(str_arg)
    print('child')

def government(str_arg):
    print(str_arg)

if __name__ == '__main__':
    place_or_company('world')
