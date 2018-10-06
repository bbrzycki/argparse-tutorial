#!/usr/bin/env python

import sys
import numpy as np
import argparse

# Physical constants in cgs units
c = 3e10
G = 7e-8

# Calculate period given semimajor axis and total mass
def find_period(a, M, use_earth_units=False):
    if use_earth_units:
        return np.sqrt(a**3 / M)
    else:
        return np.sqrt(4 * np.pi**2 * a**3 / (G * M))

# Calculate total mass given semimajor axis and period
def find_mass(a, P, use_earth_units=False):
    if use_earth_units:
        return a**3 / P**2
    else:
        return 4 * np.pi**2 * a**3 / (G * P**2)

# Calculate semimajor axis given period and total mass
def find_semimajor_axis(P, M, use_earth_units=False):
    if use_earth_units:
        return np.power(M * P**2, 1/3)
    else:
        return np.power(G * M * P**2 / (4 * np.pi**2), 1/3)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Use Kepler\'s 3rd Law to ' \
        + 'calculate things! By default, it uses cgs, but can use convenient ' \
        + 'Earth units with the -e option!')
    parser.add_argument('-a', dest='a', type=float, default=None,
                        help='Semimajor axis')
    parser.add_argument('-P', dest='P', type=float, default=None,
                        help='Period')
    parser.add_argument('-M', dest='M', type=float, default=None,
                        help='Total mass')
    parser.add_argument('-e','--use_earth_units', action='store_true',
                        help='Option to use units of 1 AU, 1 yr, and 1 solar ' \
                            + 'mass instead of cgs')

    args = parser.parse_args()

    a = args.a
    P = args.P
    M = args.M
    use_earth_units = args.use_earth_units

    if a is not None and P is not None and M is None:
        if use_earth_units:
            unit = 'solar masses'
        else:
            unit = 'g'
        print(find_mass(a, P, use_earth_units), unit)
    elif a is not None and P is None and M is not None:
        if use_earth_units:
            unit = 'yr'
        else:
            unit = 's'
        print(find_period(a, M, use_earth_units), unit)
    elif a is None and P is not None and M is not None:
        if use_earth_units:
            unit = 'AU'
        else:
            unit = 'cm'
        print(find_semimajor_axis(P, M, use_earth_units), unit)
    else:
        parser.error('Invalid parameters! Specify exactly two out of the ' \
                + 'three possible parameters: semimajor axis (a), period (P), '\
                + 'and total mass (M).')
