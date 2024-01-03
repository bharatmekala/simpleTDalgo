# RL Learning Environment

A simple reinforcement learning environment with states, connections, and Temporal Difference (TD) learning algorithms (including TD(0) and TD(λ)).

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

This project provides a basic reinforcement learning environment where an agent can move between states, receive rewards, and learn using Temporal Difference (TD) learning algorithm (TD(0)).

## Features

- States with rewards and termination conditions
- State connections for agent movement
- TD(0) and TD(λ) learning algorithms for value function updates

## Getting Started

### Prerequisites

Ensure you have the following prerequisites installed:

- Python 3.10
- NumPy
- colorama

### Installation

Clone the repository:

```bash
git clone https://github.com/your-username/rl-learning-environment.git
cd rl-learning-environment
```

### usage
```
from classes import State, TD

# Creating a 5x5 array of State objects
map_5x5 = ...

# Initializing TD algorithm with lambda value
TD_algo = TD(map_5x5, lam=0.7)

# Running the TD algorithm (e.g., TD(λ))
for _ in range(100000):
    TD_algo.td_lambda_forward()
    # Additional visualization or analysis if needed

```
