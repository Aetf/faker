
#! /usr/bin/env python

def important_fact(str_arg):
    new_fact_and_world(str_arg)
    print('world')

def new_fact_and_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    important_fact('good_company_and_last_hand')
