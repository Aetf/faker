
#! /usr/bin/env python

def government_or_child(str_arg):
    government(str_arg)
    print('government')

def government(str_arg):
    print(str_arg)

if __name__ == '__main__':
    government_or_child('bad_company')
