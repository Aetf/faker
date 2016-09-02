
#! /usr/bin/env python

def child_and_point(str_arg):
    fact(str_arg)
    print('good_work')

def fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child_and_point('small_day')
