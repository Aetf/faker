
#! /usr/bin/env python

def time_or_fact(str_arg):
    call_person(str_arg)
    print('try_person')

def call_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    time_or_fact('world')
