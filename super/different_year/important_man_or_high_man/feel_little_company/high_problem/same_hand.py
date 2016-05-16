
#! /usr/bin/env python

def child(str_arg):
    high_person(str_arg)
    print('few_time')

def high_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('tell_fact')
