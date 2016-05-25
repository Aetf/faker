
#! /usr/bin/env python

def life_or_part(str_arg):
    call_public_problem_at_eye(str_arg)
    print('part')

def call_public_problem_at_eye(str_arg):
    print(str_arg)

if __name__ == '__main__':
    life_or_part('high_work')
