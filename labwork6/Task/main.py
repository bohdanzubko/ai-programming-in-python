from simpleai.search import CspProblem, backtrack


# Define the function that imposes the constraint
# that neighbors should be different
def constraint_func(names, values):
    return values[0] != values[1]


if __name__ == '__main__':
    # Specify the variables
    names = ('Camp Nou', 'Old Trafford',
             'Anfield', 'Santiago Bernabeu',
             'Allianz Arena', 'Signal Iduna Park',
             'Emirates Stadium', 'Wembley Stadium',
             'San Siro', 'Etihad Stadium',
             'Stade de France', 'Maracana Stadium',
             'Azteca Stadium', 'Stamford Bridge')

    # Define the possible colors
    colors = dict((name, ['red', 'green', 'blue', 'purple']) for name in names)

    # Define the constraints
    constraints = [
        (('Emirates Stadium', 'Anfield'), constraint_func),
        (('Emirates Stadium', 'Santiago Bernabeu'), constraint_func),
        (('Emirates Stadium', 'Wembley Stadium'), constraint_func),
        (('Emirates Stadium', 'Stade de France'), constraint_func),
        (('Emirates Stadium', 'Maracana Stadium'), constraint_func),
        (('Emirates Stadium', 'Etihad Stadium'), constraint_func),
        (('Emirates Stadium', 'Signal Iduna Park'), constraint_func),

        (('Stade de France', 'Wembley Stadium'), constraint_func),
        (('Stade de France', 'Camp Nou'), constraint_func),
        (('Stade de France', 'San Siro'), constraint_func),
        (('Stade de France', 'Stamford Bridge'), constraint_func),
        (('Stade de France', 'Maracana Stadium'), constraint_func),

        (('Etihad Stadium', 'Signal Iduna Park'), constraint_func),
        (('Etihad Stadium', 'Maracana Stadium'), constraint_func),
        (('Etihad Stadium', 'Azteca Stadium'), constraint_func),

        (('Old Trafford', 'Anfield'), constraint_func),
        (('Old Trafford', 'Signal Iduna Park'), constraint_func),

        (('Signal Iduna Park', 'Anfield'), constraint_func),

        (('Santiago Bernabeu', 'Anfield'), constraint_func),
        (('Santiago Bernabeu', 'Wembley Stadium'), constraint_func),
        (('Santiago Bernabeu', 'Allianz Arena'), constraint_func),

        (('San Siro', 'Allianz Arena'), constraint_func),
        (('San Siro', 'Wembley Stadium'), constraint_func),
        (('San Siro', 'Camp Nou'), constraint_func),

        (('Wembley Stadium', 'Allianz Arena'), constraint_func),

        (('Stamford Bridge', 'Azteca Stadium'), constraint_func),
        (('Stamford Bridge', 'Maracana Stadium'), constraint_func),
        (('Stamford Bridge', 'Camp Nou'), constraint_func),

        (('Maracana Stadium', 'Azteca Stadium'), constraint_func),
    ]

    # Solve the problem
    problem = CspProblem(names, colors, constraints)

    # Print the solution
    output = backtrack(problem)
    print('\nColor mapping:\n')
    for k, v in output.items():
        print(k, '==>', v)
