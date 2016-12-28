
#! /usr/bin/env python

def public_life(str_arg):
    man(str_arg)
    print('life')

def man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    public_life('public_fact_and_first_man')
