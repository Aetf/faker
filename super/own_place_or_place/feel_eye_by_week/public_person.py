
#! /usr/bin/env python

def thing_and_place(str_arg):
    thing(str_arg)
    print('old_company')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing_and_place('last_way')
