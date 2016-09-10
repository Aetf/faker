
#! /usr/bin/env python

def public_man(str_arg):
    same_person(str_arg)
    print('long_case')

def same_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    public_man('fact')
