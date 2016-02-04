
#! /usr/bin/env python

def good_time_and_point(str_arg):
    company(str_arg)
    print('child')

def company(str_arg):
    print(str_arg)

if __name__ == '__main__':
    good_time_and_point('other_part')
