
#! /usr/bin/env python

def hand(str_arg):
    know_different_case_from_company(str_arg)
    print('child')

def know_different_case_from_company(str_arg):
    print(str_arg)

if __name__ == '__main__':
    hand('feel_thing')
