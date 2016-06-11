
#! /usr/bin/env python

def child(str_arg):
    use_problem_at_next_point(str_arg)
    print('hand')

def use_problem_at_next_point(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('able_year')
