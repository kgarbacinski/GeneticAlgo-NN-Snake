# GeneticAlgo-NN-Snake

## Introduction
This project is a self-learning Snake game implemented using a genetic algorithm and a custom-built multi-layer neural network.

## Installation
1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the game using `python main.py`.

## Usage
- The game will automatically start and evolve the snake using genetic algorithms.
- The current generation and score are displayed on the screen.

## Concepts
- The neural network consists of 2 hidden layers with 18 nodes each, an input layer with 24 nodes, and an output layer with 4 nodes.
- The input layer is composed of "visions" in 8 directions, each with parameters such as distance from walls, presence of an apple, and distance from the tail.
- The genetic algorithm selects the best-performing snakes for the next generation, applying crossover and mutation.

## Strategy
- The snake's score is calculated based on its lifetime and tail length: `score = life_time^2 * 2^(tail_length)`.

## Screenshots
- Generation 3:
  ![Generation 3](imgs/generation_nr_3.png)
- Generation 70:
  ![Generation 70](imgs/generation_nr_70.png)

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.
