
#! /usr/bin/env python

def thing(str_arg):
    same_case(str_arg)
    print('early_group')

def same_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('long_number')
