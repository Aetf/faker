
#! /usr/bin/env python

def big_child(str_arg):
    government(str_arg)
    print('part')

def government(str_arg):
    print(str_arg)

if __name__ == '__main__':
    big_child('case')
