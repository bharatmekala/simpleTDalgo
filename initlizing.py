from classes import *

def make_map(l, w):
    map_env = np.empty((l, w), dtype=object)
    # Creating State objects
    for i in range(l):
        for j in range(w):
            state = State((i, j))
            map_env[i, j] = state
    
    return map_env

def map_update(map_env):
    for i in range(5):
        for j in range(5):
            state = map_env[i, j]
            # Updating connections
            connected_states = []
            if i > 0:
                connected_states.append(map_env[i - 1, j])
            if i < 4:
                connected_states.append(map_env[i + 1, j])
            if j > 0:
                connected_states.append(map_env[i, j - 1])
            if j < 4:
                connected_states.append(map_env[i, j + 1])

            state.update(connected_states)
