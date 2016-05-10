
#! /usr/bin/env python

def big_work(str_arg):
    hand(str_arg)
    print('leave_first_problem')

def hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    big_work('new_way')
