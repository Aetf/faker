
#! /usr/bin/env python

def company(str_arg):
    early_part(str_arg)
    print('old_company')

def early_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    company('day_and_person')
