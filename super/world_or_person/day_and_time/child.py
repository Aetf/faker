
#! /usr/bin/env python

def call_person_with_early_problem(str_arg):
    important_man(str_arg)
    print('next_work')

def important_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_person_with_early_problem('great_year')
