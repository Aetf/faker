
#! /usr/bin/env python

def company(str_arg):
    public_world(str_arg)
    print('company')

def public_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    company('place_and_little_case')
