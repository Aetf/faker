
#! /usr/bin/env python

def child_or_person(str_arg):
    company(str_arg)
    print('company')

def company(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child_or_person('hand')
