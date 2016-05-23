
#! /usr/bin/env python

def child(str_arg):
    fact(str_arg)
    print('new_company')

def fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('say_public_problem')
