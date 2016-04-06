
#! /usr/bin/env python

def own_child(str_arg):
    person(str_arg)
    print('little_fact')

def person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    own_child('woman')
