import pickle
import numpy as np

class State:
    def __init__(self, location, reward=-0.4, terminate=False):
        self.reward = reward
        self.terminate = terminate
        self.location = location
        self.adj = []
        self.value = 0  # Initialize value

    def update(self, connected):
        """Makes a list of all other states it's connected to."""
        self.adj = connected

    def next_state(self):
        """Returns a random neighboring state."""
        if not self.adj:
            return self  # Return itself if no neighbors
        return np.random.choice(self.adj)

    def save_state(self, filename):
        """Save the state, including the value function, to a file."""
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def load_state(cls, filename):
        """Load the state, including the value function, from a file."""
        with open(filename, "rb") as file:
            loaded_state = pickle.load(file)
        return loaded_state

#TD(0) algo
class TD:
    lam = 0.7
    gam = 0.9
    alpha = 0.3
    
    def __init__(self, map):
        self.map = map
    
    def random(self):
        #picking a random spot in the array
        rows, cols = self.map.shape
        random_row = np.random.randint(0, rows)
        random_col = np.random.randint(0, cols)
        return self.map[random_row, random_col]
    
    def forward(self):
    
        #getting a random
        start = self.random()
        print(start.location)
        
        if start.terminate:
            pass
        else:
            next_state = start.next_state()
            start.value = int(start.value + self.alpha*(next_state.reward + self.gam * next_state.value - start.value))
            
        
        
        
    
    
    
        
        
        
        
        
        
        
        
    
        
        

