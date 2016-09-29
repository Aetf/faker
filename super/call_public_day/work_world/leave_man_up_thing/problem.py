
#! /usr/bin/env python

def own_life(str_arg):
    work(str_arg)
    print('person')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    own_life('person')
