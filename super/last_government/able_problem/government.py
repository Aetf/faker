
#! /usr/bin/env python

def early_man(str_arg):
    man(str_arg)
    print('different_fact')

def man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    early_man('week_and_first_thing')
