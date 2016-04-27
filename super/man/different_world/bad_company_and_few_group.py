
#! /usr/bin/env python

def own_world(str_arg):
    person(str_arg)
    print('way_and_world')

def person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    own_world('great_day')
