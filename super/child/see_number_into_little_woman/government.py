
#! /usr/bin/env python

def child(str_arg):
    person(str_arg)
    print('important_year')

def person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('call_high_work')
