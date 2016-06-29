
#! /usr/bin/env python

def work(str_arg):
    call_own_fact(str_arg)
    print('life')

def call_own_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work('important_man_or_case')
