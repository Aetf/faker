
#! /usr/bin/env python

def time(str_arg):
    great_part(str_arg)
    print('child')

def great_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    time('different_person')
