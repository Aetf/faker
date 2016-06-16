
#! /usr/bin/env python

def work(str_arg):
    woman(str_arg)
    print('different_week')

def woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work('new_company')
