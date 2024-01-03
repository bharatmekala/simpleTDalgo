from classes import *
from printing import *


#initalizing map:
map = np.empty((5, 5), dtype=object)
# Creating State objects
for i in range(5):
    for j in range(5):
        state = State((i, j))
        map[i, j] = state
map[0, 0] = State((0, 0), -100, True)
map[0, 0].value = -100
map[4, 4] = State((4, 4), 100, True)
map[4, 4].value = 100

for i in range(5):
    for j in range(5):
        state = map[i, j]
        # Updating connections (for example, connecting to neighboring states)
        connected_states = []
        if i > 0:
            connected_states.append(map[i - 1, j])
        if i < 4:
            connected_states.append(map[i + 1, j])
        if j > 0:
            connected_states.append(map[i, j - 1])
        if j < 4:
            connected_states.append(map[i, j + 1])

        state.update(connected_states)



TD_algo = TD(map)

for _ in range(10000):
    TD_algo.forward()
    color_map_print(map)

for row in map:
    for state in row:
        state.save_state("state_save/" + str(state.location))
