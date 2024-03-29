# cse571_mcts
This project is about implementing Monte Carlo Tree Search Agent in Berkeley Pacman Ai projects.

We have implemented the MCTS Algotirithm and also tweaked it to choose a better actions in simulation part.

To run the MCTSAgent --> python pacman.py -p MCTSAgent -l [choose_your_layput]
To run the BetterMCTSAgent --> python pacman.py -p BetterMCTSAgent -l [choose_your_layout]

We have created a series of layouts of size categorized into medium, large each 100. for statistically testing this MCTS, BetterMCTS Agents comparing them with Minimax, AlphaBeta Agents.

or if you want to run multiple Agents in multiple Layouts with choosen number of ghosts check out the testMcts.py file. Change this file according to your requirements and run using --> python testMcts.py


Contributors : Loga, Sachin, Nikitha, Tarun