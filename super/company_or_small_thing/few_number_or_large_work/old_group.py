
#! /usr/bin/env python

def part(str_arg):
    work_child(str_arg)
    print('part')

def work_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    part('last_point')
