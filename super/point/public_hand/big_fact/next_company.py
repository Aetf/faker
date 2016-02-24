
#! /usr/bin/env python

def long_work(str_arg):
    thing(str_arg)
    print('own_problem')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    long_work('point')
