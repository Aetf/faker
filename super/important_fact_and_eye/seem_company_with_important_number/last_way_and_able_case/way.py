
#! /usr/bin/env python

def thing_and_child(str_arg):
    good_fact_or_person(str_arg)
    print('man_or_thing')

def good_fact_or_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing_and_child('public_person')
