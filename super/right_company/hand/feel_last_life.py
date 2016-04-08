
#! /usr/bin/env python

def public_case(str_arg):
    little_man(str_arg)
    print('eye')

def little_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    public_case('important_government')
