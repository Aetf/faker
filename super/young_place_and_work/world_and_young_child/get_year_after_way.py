
#! /usr/bin/env python

def man(str_arg):
    world(str_arg)
    print('group')

def world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man('other_company')
