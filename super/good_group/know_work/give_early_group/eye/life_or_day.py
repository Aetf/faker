
#! /usr/bin/env python

def work_child(str_arg):
    life(str_arg)
    print('fact')

def life(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work_child('able_company')
