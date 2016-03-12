
#! /usr/bin/env python

def different_world(str_arg):
    person(str_arg)
    print('government')

def person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    different_world('try_able_day')
