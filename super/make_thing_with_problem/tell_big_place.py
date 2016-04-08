
#! /usr/bin/env python

def old_person(str_arg):
    child(str_arg)
    print('other_person_or_group')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    old_person('early_case_and_life')
