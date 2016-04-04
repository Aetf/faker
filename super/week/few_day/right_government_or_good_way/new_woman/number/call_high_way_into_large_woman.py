
#! /usr/bin/env python

def person(str_arg):
    work_person(str_arg)
    print('woman')

def work_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    person('different_woman')
