
#! /usr/bin/env python

def fact(str_arg):
    own_fact_or_large_group(str_arg)
    print('early_group')

def own_fact_or_large_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    fact('big_time_and_number')
