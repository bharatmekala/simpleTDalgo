from classes import *
from initlizing import *
from printing import *

#creating a 5 x 5 map env
map_env = make_map(5, 5)

#making top left corner bad
map_env[0, 0] = State((0, 0), -100, True)
map_env[0, 0].value = -200
#bottom right corner good
map_env[4, 4] = State((4, 4), 100, True)
map_env[4, 4].value = 200

#adds connections to map_env
map_update(map_env)

#initalized TD algo
TD_algo = TD(map_env)

#runs algo, prining progress
for _ in range(10000):
    TD_algo.forward()
    color_map_print(map_env)

#dumps all data into /state_save
for row in map_env:
    for state in row:
        state.save_state("state_save/" + str(state.location))
