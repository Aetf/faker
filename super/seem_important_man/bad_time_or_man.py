
#! /usr/bin/env python

def other_day(str_arg):
    day(str_arg)
    print('leave_way')

def day(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_day('other_man')
