
#! /usr/bin/env python

def child(str_arg):
    company(str_arg)
    print('old_place')

def company(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('point_or_important_fact')
