
#! /usr/bin/env python

def hand(str_arg):
    work(str_arg)
    print('next_person')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    hand('group')
