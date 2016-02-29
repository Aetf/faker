
#! /usr/bin/env python

def use_fact_in_case(str_arg):
    thing(str_arg)
    print('way')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    use_fact_in_case('small_work')
