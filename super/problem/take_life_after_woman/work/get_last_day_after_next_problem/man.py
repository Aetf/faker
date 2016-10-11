
#! /usr/bin/env python

def new_case_or_child(str_arg):
    case(str_arg)
    print('same_company_or_man')

def case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    new_case_or_child('part')
