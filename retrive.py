from classes import *
from printing import *

map = np.empty((5, 5), dtype=object)
# Creating State objects
for i in range(5):
    for j in range(5):
        location = (i, j)
        state = State(location).load_state("state_save/" + str(location))
        map[i, j] = state

color_map_print(map)



