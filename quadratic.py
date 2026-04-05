# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):


    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        return f"({r1}, {r2})"
    elif discriminante == 0:
        r12 = -b / (2* a)
        return f"({r12})"
    elif discriminante < 0 :
        return f"()"

def value_y(a, b, c, x):
    y = a*(x**2) + b*x +c
    return y

def to_string(a, b, c):

    return f"f(x) = {a} * X^2 + {b} * X + {c}"



def derivation(a, b, c):
    g = 2 * a
    return f"f'(x) = {g} * X + {b}"

