
#! /usr/bin/env python

def hand_or_company(str_arg):
    company(str_arg)
    print('child')

def company(str_arg):
    print(str_arg)

if __name__ == '__main__':
    hand_or_company('use_other_person')
