
#! /usr/bin/env python

def public_hand(str_arg):
    company(str_arg)
    print('world')

def company(str_arg):
    print(str_arg)

if __name__ == '__main__':
    public_hand('way_and_good_year')
