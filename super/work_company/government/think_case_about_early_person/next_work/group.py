
#! /usr/bin/env python

def child(str_arg):
    point_or_person(str_arg)
    print('different_world')

def point_or_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('old_problem')
