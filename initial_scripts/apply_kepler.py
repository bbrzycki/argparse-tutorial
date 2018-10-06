import kepler

# Let's calculate the orbital radius of Jupiter!
jupiter_semimajor = kepler.find_semimajor_axis(11.86, 1, use_earth_units=True)
print('Jupiter is around %2.2f AU from the Sun.' % jupiter_semimajor)
