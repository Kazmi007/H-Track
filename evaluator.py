
# get_data() and the random seed can be modified to the user's preference.

import random
random.seed(111)




def get_data():
	"""Get the initial state of the individuals & the environment"""
	# @TODO: Update this function just for your own testing.
	       #[M, N,   D,   K, LAMBDA, MU,    universal_state]
	return [50, 100, 5, 80, 30, 0.55, [[(3, 38), 0, 'notmasked', 'infected'], [(7, 41), 1, 'notmasked', 'infected'], [(92, 41), 7, 'notmasked', 'infected'], [(1, 43), 2, 'notmasked', 'notinfected'], [(98, 44), 6, 'notmasked', 'notinfected'], [(8, 45), 2, 'notmasked', 'infected'], [(91, 45), 6, 'notmasked', 'infected'], [(2, 47), 1, 'notmasked', 'notinfected'], [(6, 48), 0, 'notmasked', 'notinfected'], [(91, 48), 6, 'notmasked', 'infected'], [(97, 48), 7, 'notmasked', 'notinfected']]]