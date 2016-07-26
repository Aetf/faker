
#! /usr/bin/env python

def woman(str_arg):
    man(str_arg)
    print('government')

def man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    woman('other_company')
