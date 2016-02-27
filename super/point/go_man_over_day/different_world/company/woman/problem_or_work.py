
#! /usr/bin/env python

def call_fact(str_arg):
    early_thing_or_case(str_arg)
    print('life')

def early_thing_or_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_fact('child')
