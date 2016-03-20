
#! /usr/bin/env python

def child(str_arg):
    get_year(str_arg)
    print('person_or_great_child')

def get_year(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('bad_company')
