from constraint import *

def solve_cryptarithmetic():
    # Create a new problem instance
    problem = Problem()

    # Add variables representing the letters
    problem.addVariables(['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y'], range(10))

    # Add constraints to ensure uniqueness of digits
    problem.addConstraint(AllDifferentConstraint(), ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y'])

    # Add constraints to enforce the puzzle rules
    problem.addConstraint(lambda s, e, n, d, m, o, r, y: s != 0 and m != 0,
                         ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y'])
    problem.addConstraint(lambda s, e, n, d, m, o, r, y: (s * 1000 + e * 100 + n * 10 + d) + (m * 1000 + o * 100 + r * 10 + e) ==
                                                      (m * 10000 + o * 1000 + n * 100 + e * 10 + y),
                         ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y'])

    # Solve the problem
    solutions = problem.getSolutions()

    # Print the solutions
    for solution in solutions:
        print("Solution:")
        print("SEND =", solution['S'], solution['E'], solution['N'], solution['D'])
        print("MORE =", solution['M'], solution['O'], solution['R'], solution['E'])
        print("MONEY =", solution['M'], solution['O'], solution['N'], solution['E'], solution['Y'])
        print()

# Solve the cryptarithmetic problem
solve_cryptarithmetic()
