
#! /usr/bin/env python

def company(str_arg):
    way(str_arg)
    print('child')

def way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    company('group_and_problem')
