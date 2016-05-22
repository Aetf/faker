
#! /usr/bin/env python

def great_company_and_different_child(str_arg):
    little_day(str_arg)
    print('other_way')

def little_day(str_arg):
    print(str_arg)

if __name__ == '__main__':
    great_company_and_different_child('other_time')
