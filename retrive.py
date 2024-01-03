from classes import *
from printing import *

#example workflow to retrive data from last traning session


map = np.empty((5, 5), dtype=object)
# Creating State objects
for i in range(5):
    for j in range(5):
        location = (i, j)
        state = State(location).load_state("state_save/" + str(location))
        map[i, j] = state

color_map_print(map)



