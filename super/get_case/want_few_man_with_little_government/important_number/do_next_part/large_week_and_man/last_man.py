
#! /usr/bin/env python

def different_person(str_arg):
    person(str_arg)
    print('same_number_and_own_number')

def person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    different_person('own_man')
