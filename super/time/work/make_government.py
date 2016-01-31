
#! /usr/bin/env python

def person(str_arg):
    want_child(str_arg)
    print('person')

def want_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    person('hand_and_case')
