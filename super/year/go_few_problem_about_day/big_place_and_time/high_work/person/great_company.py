
#! /usr/bin/env python

def woman(str_arg):
    public_case_and_fact(str_arg)
    print('world')

def public_case_and_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    woman('fact')
