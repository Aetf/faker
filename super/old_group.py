
#! /usr/bin/env python

def public_way(str_arg):
    child(str_arg)
    print('eye')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    public_way('first_thing_and_company')
