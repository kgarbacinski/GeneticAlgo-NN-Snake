# GeneticAlgo-NN-Snake

# Introduction
That's a self-teaching Snake game made with genetic algorithm and own-implemented MultiLayer Neural Network. 

# Game Screenshots
- Generation 3:
![Gen 3](https://github.com/kgarbacinski/GeneticAlgo-NN-Snake/blob/master/Gen%203.PNG)
![Gen 4](https://github.com/kgarbacinski/GeneticAlgo-NN-Snake/blob/master/Gen%2070.PNG)

# Concepts
- NN's been made with 2 hidden layers (each 18 nodes), input layer's 24 nodes and the output one contains 4 nodes (each one is the snake's move direction) 
- Input layer is a set of "visions" in each 8 directions (left, up, right, down and diagonally ones)
- Each vision has parameters like distance from walls, is an apple on snake's way and distance from its tail
- The strategy of learning is to create as many snakes in one population as your processor is able to and choose the best one (with the highest fitness score), 
place it into the next generation and crossover/mutate the other snakes as well
- The mutation process has been made with uniform strategy
- As said before, a NN has been created from scratch, therefore it was necessary to apply process of calculation a matrix dot product, applying activation (sigmoid) function etc.

# Strategy
As the snake's living time and his tail is getting longer, the snake's score is getting higher. Score is computed from formula: score = life_time ^ 2 * 2 ^ (tail_length)  
