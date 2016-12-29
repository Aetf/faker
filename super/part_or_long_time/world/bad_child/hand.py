
#! /usr/bin/env python

def thing(str_arg):
    person_and_government(str_arg)
    print('public_person_and_few_time')

def person_and_government(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('woman')
