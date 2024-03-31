# Monte Carlo Tree Search Implementation for Pacman

### Reference Paper: Browne, Cameron B., et al. "A survey of Monte Carlo tree search methods. IEEE Transactions on Computational Intelligence and AI in games 4.1 (2012): 1-43
This project implements two Monte Carlo Tree Search Agents for the UC Berkeley Pacman AI domain.

We have implemented the vanilla MCTS Algorithm as the first agent (MCTSAgent) and have tweaked it to choose a better actions in the simulation step in the second agent (BetterMCTSAgent).

To run the **MCTSAgent**:

`python pacman.py -p MCTSAgent -l [choose_your_layout]`

To run the **BetterMCTSAgent**:

`python pacman.py -p BetterMCTSAgent -l [choose_your_layout]`

We have created a series of layout sizes categorized into small, medium and large (30 each). These layouts have been used for statistically comparing the MCTS and BetterMCTS agents with Alpha-Beta Minimax and Expectimax agents.

You can also run multiple agents in multiple layouts with chosen number of ghosts using the testMcts.py file. 

Change this file according to your requirements and run using:

`python testMcts.py`

The statistical analyses performed for the comparisons have been captured in the `analysis` folder. We have included a iPython notebook with all the statistical visualizations and a `winPercent.py` file that calculates the win percentage from the console output. 

Contributors : Sachin, Nikitha, Loga, and Tarun