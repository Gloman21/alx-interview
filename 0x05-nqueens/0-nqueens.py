#!/usr/bin/python3
"""
N queens
"""

import sys

if len(sys.argv) != 2:
    print('Usage: nqueens N')
    exit(1)

<<<<<<< HEAD
try:
    n_q = int(sys.argv[1])
except ValueError:
    print('N must be a number')
    exit(1)

if n_q < 4:
    print('N must be at least 4')
    exit(1)


def solve_nqueens(n):
    '''Self descriptive'''
    if n == 0:
        return [[]]
    inner_solution = solve_nqueens(n - 1)
    return [solution + [(n, i + 1)]
            for i in range(n_q)
            for solution in inner_solution
            if safe_queen((n, i + 1), solution)]


def attack_queen(square, queen):
    '''Self descriptive'''
    (row1, col1) = square
    (row2, col2) = queen
    return (row1 == row2) or (col1 == col2) or\
        abs(row1 - row2) == abs(col1 - col2)


def safe_queen(sqr, queens):
    '''Self descriptive'''
    for queen in queens:
        if attack_queen(sqr, queen):
            return False
    return True


for answer in reversed(solve_nqueens(n_q)):
    result = []
    for p in [list(p) for p in answer]:
        result.append([i - 1 for i in p])
    print(result)
=======
    try:
        a_q = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if a_q < 4:
        print('N must be at least 4')
        exit(1)


    def solve_nqueens(n):
        '''Self descriptive'''
        if n == 0:
            return [[]]
        inner_solution = solve_nqueens(n - 1)
        return [solution + [(n, i + 1)]
                for i in range (a_q)
                for solution in inner_solution
                if safe_queen((n, i + 1), solution)]


    def attack_queen(square, quen):
        '''Self descriptive'''
        (row1, col1) = square
        (row2, col2) = queen
        return (row1 == row2) or (col1 == col2) or\
                abs(row1 - row2) == abs(col1 - col2)



    def safe_queen(sqr, queens):
        '''Self descriptive'''
        for queen in queens:
            if attack_queen(sqr, queen):
                return False
            return True



    for answer in reversed(solved_nqueens(a_q)):
        result = []
        for p in [list(p) for p in answer]:
            result.append([i -1 for i in p])
        print(result)

>>>>>>> 05dd36c46e6f0484b388f3854461344ca7f331c6