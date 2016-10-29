
#! /usr/bin/env python

def child(str_arg):
    big_place(str_arg)
    print('same_thing')

def big_place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('person_or_time')
