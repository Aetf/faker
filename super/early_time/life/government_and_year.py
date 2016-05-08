
#! /usr/bin/env python

def thing(str_arg):
    hand_and_company(str_arg)
    print('child')

def hand_and_company(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('give_man')
