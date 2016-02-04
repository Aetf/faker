
#! /usr/bin/env python

def great_fact(str_arg):
    important_fact(str_arg)
    print('bad_child')

def important_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    great_fact('hand')
