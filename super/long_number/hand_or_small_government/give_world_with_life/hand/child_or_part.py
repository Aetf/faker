
#! /usr/bin/env python

def bad_company(str_arg):
    great_world(str_arg)
    print('world')

def great_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_company('eye_and_thing')
