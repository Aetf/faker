
#! /usr/bin/env python

def person_and_point(str_arg):
    call_same_way(str_arg)
    print('child')

def call_same_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    person_and_point('fact')
