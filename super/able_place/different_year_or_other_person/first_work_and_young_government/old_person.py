
#! /usr/bin/env python

def child(str_arg):
    great_person(str_arg)
    print('new_problem')

def great_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('be_early_life_into_own_child')
