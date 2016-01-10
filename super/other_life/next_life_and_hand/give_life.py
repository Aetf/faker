
#! /usr/bin/env python

def man(str_arg):
    company(str_arg)
    print('woman')

def company(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man('child')
