
#! /usr/bin/env python

def company(str_arg):
    long_part(str_arg)
    print('child')

def long_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    company('give_problem')
