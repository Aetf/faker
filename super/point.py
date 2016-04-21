
#! /usr/bin/env python

def work_first_person_on_group(str_arg):
    number(str_arg)
    print('other_way')

def number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work_first_person_on_group('thing')
