
#! /usr/bin/env python

def time_and_public_child(str_arg):
    find_new_fact_in_little_thing(str_arg)
    print('child')

def find_new_fact_in_little_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    time_and_public_child('have_public_company')
