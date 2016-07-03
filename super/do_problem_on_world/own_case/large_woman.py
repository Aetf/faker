
#! /usr/bin/env python

def child(str_arg):
    child(str_arg)
    print('group_and_part')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('able_place_or_important_problem')
