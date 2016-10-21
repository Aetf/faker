
#! /usr/bin/env python

def be_early_child(str_arg):
    fact(str_arg)
    print('way')

def fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    be_early_child('work_day_to_problem')
