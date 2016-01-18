
#! /usr/bin/env python

def use_work_at_world(str_arg):
    government(str_arg)
    print('government')

def government(str_arg):
    print(str_arg)

if __name__ == '__main__':
    use_work_at_world('first_work')
