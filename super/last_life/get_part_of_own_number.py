
#! /usr/bin/env python

def own_man(str_arg):
    person(str_arg)
    print('know_man')

def person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    own_man('world')
