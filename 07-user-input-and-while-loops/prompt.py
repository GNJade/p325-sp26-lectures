from numpy.lib.scimath import sqrt

# ask for the three coefficients to use the quadratic formula
response = input('Enter a, b, c: ')

a, b, c = eval(response)

solution_1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
solution_2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
print(f'Solution 1: {solution_1} \nSolution 2: {solution_2}')