
#! /usr/bin/env python

def work(str_arg):
    person(str_arg)
    print('person')

def person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work('time_and_first_way')
