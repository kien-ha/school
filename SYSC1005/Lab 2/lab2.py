import math


def area_of_disk(r):
    """Return the area of a ring with radius r"""
    return math.pi * r ** 2


def area_of_ring(outer, inner):
    """Returns the area of the ring

    Return the area of the outer ring with radius outer.
    The radius of the hole is inner.
    """
    return area_of_disk(outer) - area_of_disk(inner)


def area_of_cone(h, r):
    """Returns the lateral surface area of a right circular cone with height h and radius r"""
    return math.pi * r * math.sqrt(r ** 2 + h ** 2)


def volume_of_sphere(r):
    """Return the volume of a sphere with the radius r"""
    return (4/3) * math.pi * r ** 3


def hollow_sphere(bigger, smaller):
    """Return the volume of the smaller sphere within the bigger sphere"""
    return volume_of_sphere(bigger) - volume_of_sphere(smaller)
