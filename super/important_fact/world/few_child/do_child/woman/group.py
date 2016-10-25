
#! /usr/bin/env python

def person(str_arg):
    child(str_arg)
    print('do_person')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    person('see_good_government')
