
#! /usr/bin/env python

def do_little_part(str_arg):
    person(str_arg)
    print('person_or_long_part')

def person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    do_little_part('first_point')
