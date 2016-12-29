
#! /usr/bin/env python

def see_child(str_arg):
    high_problem(str_arg)
    print('problem')

def high_problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    see_child('able_eye_or_other_problem')
