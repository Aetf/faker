
#! /usr/bin/env python

def child(str_arg):
    small_problem(str_arg)
    print('come_thing_at_eye')

def small_problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('number_and_life')
