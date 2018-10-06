import numpy as np

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

print('Calculating the orbital radius of our Earth...')

orbital_radius_cm = find_semimajor_axis(60*60*24*365.25, 2e33)
orbital_radius_AU = find_semimajor_axis(1, 1, use_earth_units=True)

print('%s AU is equal to %2.2e cm.' % (orbital_radius_AU, orbital_radius_cm))
