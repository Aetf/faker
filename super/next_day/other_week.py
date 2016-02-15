
#! /usr/bin/env python

def ask_work(str_arg):
    fact(str_arg)
    print('do_thing_with_small_fact')

def fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    ask_work('person')
