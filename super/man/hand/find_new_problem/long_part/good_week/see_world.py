
#! /usr/bin/env python

def able_work(str_arg):
    woman(str_arg)
    print('woman')

def woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    able_work('child')
