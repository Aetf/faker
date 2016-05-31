
#! /usr/bin/env python

def fact_or_child(str_arg):
    child(str_arg)
    print('fact')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    fact_or_child('look_person_for_small_day')
