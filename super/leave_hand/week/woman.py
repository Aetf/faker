
#! /usr/bin/env python

def world_or_company(str_arg):
    company(str_arg)
    print('important_child')

def company(str_arg):
    print(str_arg)

if __name__ == '__main__':
    world_or_company('eye_and_small_week')
