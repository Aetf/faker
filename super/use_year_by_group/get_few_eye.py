
#! /usr/bin/env python

def tell_problem_from_fact(str_arg):
    part(str_arg)
    print('public_child')

def part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    tell_problem_from_fact('give_year')
