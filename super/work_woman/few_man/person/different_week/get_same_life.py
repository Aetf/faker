
#! /usr/bin/env python

def use_other_problem(str_arg):
    life_or_last_fact(str_arg)
    print('part')

def life_or_last_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    use_other_problem('call_fact')
