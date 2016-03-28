
#! /usr/bin/env python

def use_problem(str_arg):
    find_person(str_arg)
    print('world')

def find_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    use_problem('long_day_or_year')
