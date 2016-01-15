
#! /usr/bin/env python

def say_thing(str_arg):
    say_important_fact(str_arg)
    print('government')

def say_important_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    say_thing('bad_work')
