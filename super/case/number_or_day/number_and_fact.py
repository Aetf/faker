
#! /usr/bin/env python

def child_or_world(str_arg):
    work_or_little_company(str_arg)
    print('young_thing')

def work_or_little_company(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child_or_world('have_government')
