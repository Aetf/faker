
#! /usr/bin/env python

def life(str_arg):
    public_way(str_arg)
    print('child')

def public_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    life('leave_different_year_with_good_problem')
