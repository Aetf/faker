
#! /usr/bin/env python

def try_fact(str_arg):
    work(str_arg)
    print('world')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    try_fact('want_problem')
