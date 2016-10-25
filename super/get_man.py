
#! /usr/bin/env python

def able_child(str_arg):
    right_child_or_other_child(str_arg)
    print('part')

def right_child_or_other_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    able_child('little_fact_and_able_point')
