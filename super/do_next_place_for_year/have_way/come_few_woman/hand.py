
#! /usr/bin/env python

def important_child(str_arg):
    little_case(str_arg)
    print('large_fact')

def little_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    important_child('man')
