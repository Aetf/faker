
#! /usr/bin/env python

def fact_and_same_way(str_arg):
    place(str_arg)
    print('other_group')

def place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    fact_and_same_way('year')
