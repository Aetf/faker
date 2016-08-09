
#! /usr/bin/env python

def early_fact_and_child(str_arg):
    man_and_same_place(str_arg)
    print('other_case')

def man_and_same_place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    early_fact_and_child('woman')
