
#! /usr/bin/env python

def own_work(str_arg):
    child(str_arg)
    print('first_fact')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    own_work('person')
