
#! /usr/bin/env python

def hand(str_arg):
    woman(str_arg)
    print('old_company')

def woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    hand('thing')
