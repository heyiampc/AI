from unification import unify

# Example usage
x = ['x', 'c', 'a']
y = ['f', 'd', 'B']
theta = unify(x, y)
print(theta)
if theta is not None and isinstance(theta, dict):
    print("Substitution:")
    for var, value in theta.items():
        print(var, "=", value)
else:
    print("Unification failed.")

    
# >>> from unification import *
# >>> unify(1, 1)
# {}
# >>> unify(1, 2)
# False
# >>> x = var('x')

# >>> unify((1, x), (1, 2))
# {~x: 2}

# >>> unify((x, x), (1, 2))
# False
