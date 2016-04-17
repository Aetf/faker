
#! /usr/bin/env python

def other_child(str_arg):
    early_person_or_way(str_arg)
    print('first_fact')

def early_person_or_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_child('high_case')
