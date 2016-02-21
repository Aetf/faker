
#! /usr/bin/env python

def little_child(str_arg):
    number(str_arg)
    print('world')

def number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    little_child('few_case')
