import math


def quadratic_roots(a, b, c):
    """
    returns the values from the quadratic formula
    """
    positive_value = (-b + math.sqrt(b ** 2 - (4 * a * c))) / (2 * a)
    negative_value = (-b - math.sqrt(b ** 2 - (4 * a * c))) / (2 * a)
    return (positive_value, negative_value)


def make_change(amount_received, amount_due):
    """
    returns the amount of change in dollars, quarters, dimes, nickels, and pennies
    """
    amount_difference = (amount_received - amount_due)
    amount_change_dollars = (amount_difference // 100)
    amount_change_quarters = (amount_difference % 100) // 25
    amount_change_dimes = (amount_difference % 100 % 25) // 10
    amount_change_nickels = (amount_difference % 100 % 25 % 10) // 5
    amount_change_pennies = (amount_difference % 100 % 25 % 10 % 5) // 1

    return (amount_change_dollars, amount_change_quarters, amount_change_dimes,
    amount_change_nickels, amount_change_pennies)


def area_of_disk(r):
        """
        Return the area of a ring with radius r.
        """
        return math.pi * r ** 2


def area_of_ring(outer, inner):
        """
        Return the area of a ring with radius outer.
        The radius of the hole is inner.
        """
        return area_of_disk(outer) - area_of_disk(inner)


def circumference(r):
    return 2 * math.pi * r


def area_of_pipe(pipe_inner_radius, length_of_pipe, pipe_thickness):

    area_of_end_ring = 2 * area_of_ring(pipe_thickness + pipe_inner_radius, pipe_inner_radius)

    area_outer_length = circumference(pipe_thickness + pipe_inner_radius) * length_of_pipe

    area_inner_length = circumference(pipe_inner_radius) * length_of_pipe

    return area_of_end_ring + area_outer_length + area_inner_length

#Tests for quadratic_roots function
quadratic_roots_test1 = quadratic_roots(1, -4, -21)
quadratic_roots_test2 = quadratic_roots(4, 12, 9)
print ("Expected value of quadratic_roots_test1: 7.0 & -3.0")
print ("Expected value of quadratic_roots_test2: -1.5 & -1.5")
print ("quadratic_roots_test1:", quadratic_roots_test1)
print ("quadratic_roots_test2:", quadratic_roots_test2)