
#! /usr/bin/env python

def great_company_and_other_problem(str_arg):
    old_way(str_arg)
    print('little_way')

def old_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    great_company_and_other_problem('different_company')
