
#! /usr/bin/env python

def different_group(str_arg):
    case(str_arg)
    print('public_part')

def case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    different_group('want_long_number')
