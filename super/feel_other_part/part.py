
#! /usr/bin/env python

def work(str_arg):
    big_fact(str_arg)
    print('public_world')

def big_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work('year')
