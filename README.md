# Falling Sand Simulation

The Falling Sand Simulation is inspired by **Noita** which uses Nolla Games' in-house `"Falling Everything"` game-engine. The code uses cellular automata where every cell has a state to imitate the effects of a falling sand. Every pixel is physically simulated allowing the user to have an in-depth simulation experience.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Cellular Automata](#cellular-automata)
- [Sand Rules](#sand-rules)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project is a simple 2D falling sand simulation created using Python and the Pygame library. The code implements a Grid class to manage the sand particles, updating their positions and handling interactions. Falling sand particles are visually simulated to react with the environment, creating captivating and natural patterns.

## Features

- **Physics-based Simulation:** Sand particles fall due to gravity and interact with one another, accurately replicating real-world sand dynamics.
- **Grid-Based Particle Management:** An optimized grid-based system efficiently manages particle positions and movements for smooth performance.
- **Interactive Design:** Users can directly add sand particles by clicking and holding the left mouse button within the interface.
- **Visually Appealing:** The sand particles gradually shift colors every few seconds, enhancing the simulation with a visually captivating effect for users.

## Cellular Automata

**Cellular automata (CA)** are discrete models used in computational theory, consisting of a grid of cells, each in one of a finite number of states. The state of each cell is determined by a set of rules based on the states of neighboring cells. This concept was first introduced in the 1940s by Stanislaw Ulam and John von Neumann.

A cellular automaton operates on a grid, which can be of any finite number of dimensions. Each cell in the grid has a state, and the state of each cell at the next time step is determined by a fixed rule that considers the current state of the cell and the states of its neighbors. The most common types of neighborhoods are the von Neumann neighborhood and the Moore neighborhood.

**Sourced from:** [Cellular automaton - Wikipedia](https://en.wikipedia.org/wiki/Cellular_automaton)

## Sand Rules

Here are the rules the simulation will follow:

1. The sand will fall one cell down if the cell below it is empty.
2. If the cell below is occupied, the sand will attempt to move right or left.
3. If there is no where to move, the sand will stay put.

## Requirements

- Python 3.x
- Pygame

## Installation

1. Clone the repository:

```powershell
git clone https://github.com/klaus-001/falling-sand-simulation.git
```

2. Install dependecies:

```powershell
pip install pygame
```

## Usage

To run the program, execute the following command in your terminal:

```powershell
python main.py
```

## Contributing

Contributions are welcome! Feel free to fork this repository, make changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is distributed under the MIT License. See [License](LICENSE.md) for more details.

