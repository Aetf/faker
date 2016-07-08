
#! /usr/bin/env python

def time(str_arg):
    man(str_arg)
    print('child')

def man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    time('same_problem')
