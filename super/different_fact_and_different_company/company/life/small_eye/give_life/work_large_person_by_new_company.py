
#! /usr/bin/env python

def work_and_bad_person(str_arg):
    group(str_arg)
    print('same_person')

def group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work_and_bad_person('make_first_problem')
