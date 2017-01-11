
#! /usr/bin/env python

def other_day(str_arg):
    different_person(str_arg)
    print('different_way')

def different_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_day('bad_year')
