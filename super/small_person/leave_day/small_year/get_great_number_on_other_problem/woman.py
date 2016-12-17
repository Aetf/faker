
#! /usr/bin/env python

def want_person(str_arg):
    woman(str_arg)
    print('person')

def woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    want_person('able_woman_or_same_eye')
