
#! /usr/bin/env python

def good_place(str_arg):
    public_child(str_arg)
    print('same_person')

def public_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    good_place('place')
