
#! /usr/bin/env python

def seem_time(str_arg):
    work(str_arg)
    print('child')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    seem_time('feel_good_number_by_problem')
