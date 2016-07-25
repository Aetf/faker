
#! /usr/bin/env python

def little_part(str_arg):
    big_way(str_arg)
    print('see_problem')

def big_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    little_part('person_or_few_part')
