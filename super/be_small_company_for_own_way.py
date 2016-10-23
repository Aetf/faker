
#! /usr/bin/env python

def important_group(str_arg):
    work_or_child(str_arg)
    print('next_part')

def work_or_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    important_group('life')
