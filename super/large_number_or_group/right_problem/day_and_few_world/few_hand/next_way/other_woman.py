
#! /usr/bin/env python

def life_and_company(str_arg):
    company(str_arg)
    print('world')

def company(str_arg):
    print(str_arg)

if __name__ == '__main__':
    life_and_company('old_eye')
