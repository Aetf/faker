
#! /usr/bin/env python

def group(str_arg):
    good_part(str_arg)
    print('public_part')

def good_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    group('long_fact')
