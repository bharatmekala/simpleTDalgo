from classes import *
from printing import *

#example workflow to retrive data from last traning session, and using it to make a policy


map_env = np.empty((5, 5), dtype=object)
# Creating State objects
for i in range(5):
    for j in range(5):
        location = (i, j)
        state = State(location).load_state("state_save/" + str(location))
        map_env[i, j] = state

color_map_print(map_env)

#creating a policy
policy = {}

for row in map_env:
    for state in row:
        policy[state] = max(state.adj, key=lambda x: x.value)

policy[map_env[0][0]] = None
policy[map_env[4][4]] = None


        



