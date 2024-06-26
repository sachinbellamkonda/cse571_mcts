# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util
from math import sqrt
import math

from game import Agent


class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)  # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        """
        We are going to consider two items, ghostdistances and fooddistances.

        We will return INT_MIN value if ghost is very close that is distance is less or equal to 2.
        And also for score to return we will return sum of inverse of foodscores - sum of inverse of ghost manhattan distance
        """

        if successorGameState.isWin():
            return float('inf')

        newFoodPos = newFood.asList()
        closestFoodDist = float('inf')
        for foodPos in newFoodPos:
            closestFoodDist = min(manhattanDistance(foodPos, newPos), closestFoodDist)
        score = - 2 * closestFoodDist - 100 * len(newFoodPos)

        minGhostDistance = float('inf')
        for ghost in newGhostStates:
            if ghost.scaredTimer == 0:
                ghostDistance = manhattanDistance(ghost.getPosition(), newPos)
                if ghostDistance < 2:
                    return float('-inf')
                minGhostDistance = min(ghostDistance, minGhostDistance)

        return score


def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def minimaxAlgo(self, gameState, depth, maximizingPlayer):
        if depth == self.depth or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)

        legalActions = gameState.getLegalActions(maximizingPlayer)

        if not legalActions:
            return self.evaluationFunction(gameState)

        if maximizingPlayer == 0:
            maxEval = float('-inf')
            for action in legalActions:
                currentValue = self.minimaxAlgo(gameState.generateSuccessor(maximizingPlayer, action), depth,
                                                maximizingPlayer + 1)
                maxEval = max(maxEval, currentValue)
            return maxEval

        else:
            minEval = float('inf')
            for action in legalActions:
                if maximizingPlayer == gameState.getNumAgents() - 1:
                    currentValue = self.minimaxAlgo(gameState.generateSuccessor(maximizingPlayer, action), depth + 1, 0)
                else:
                    currentValue = self.minimaxAlgo(gameState.generateSuccessor(maximizingPlayer, action), depth,
                                                    maximizingPlayer + 1)
                minEval = min(minEval, currentValue)
            return minEval

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"

        bestScore = float('-inf')
        bestAction = None
        legalActions = gameState.getLegalActions(0)
        for action in legalActions:
            score = self.minimaxAlgo(gameState.generateSuccessor(0, action), 0, 1)
            if score > bestScore:
                bestScore = score
                bestAction = action
        return bestAction

        util.raiseNotDefined()


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def max_player(self, gameState, depth, maximiZingPlayer, alpha, beta):
        if depth == self.depth or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)

        legalActions = gameState.getLegalActions(maximiZingPlayer)

        if not legalActions:
            return self.evaluationFunction(gameState)

        maxEval = float('-inf')
        for action in legalActions:
            eval = self.min_player(gameState.generateSuccessor(0, action), depth, maximiZingPlayer + 1, alpha, beta)
            maxEval = max(maxEval, eval)
            if beta < maxEval:
                break
            alpha = max(maxEval, alpha)
        return maxEval

    def min_player(self, gameState, depth, maximizingPlayer, alpha, beta):

        if gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)

        minEval = float('inf')

        legalActions = gameState.getLegalActions(maximizingPlayer)

        if not legalActions:
            return self.evaluationFunction(gameState)

        for action in legalActions:
            if maximizingPlayer == (gameState.getNumAgents() - 1):
                eval = self.max_player(gameState.generateSuccessor(maximizingPlayer, action), depth + 1, 0, alpha, beta)
                minEval = min(minEval, eval)
                if minEval < alpha:
                    break
                beta = min(beta, minEval)
            else:
                eval = self.min_player(gameState.generateSuccessor(maximizingPlayer, action), depth,
                                       maximizingPlayer + 1, alpha, beta)
                minEval = min(minEval, eval)
                if minEval < alpha:
                    break
                beta = min(beta, minEval)
        return minEval

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        alpha = float('-inf')
        beta = float('inf')
        bestAction = None
        bestScore = float('-inf')
        legalActions = gameState.getLegalActions(0)
        for action in legalActions:
            score = self.min_player(gameState.generateSuccessor(0, action), 0, 1, alpha, beta)
            if score > bestScore:
                bestScore = score
                bestAction = action
            if beta < score:
                break
            alpha = max(alpha, score)
        return bestAction
        util.raiseNotDefined()


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def max_palyer(self, gameState, depth, maximizingPlayer):
        if depth == self.depth or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)

        legalActions = gameState.getLegalActions(maximizingPlayer)

        maxEval = float('-inf')
        for action in legalActions:
            currentValue = self.ecpecti_player(gameState.generateSuccessor(maximizingPlayer, action), depth,
                                               maximizingPlayer + 1)
            maxEval = max(maxEval, currentValue)

        return maxEval

    def ecpecti_player(self, gameState, depth, maximizingPlayer):
        if gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)

        legalActions = gameState.getLegalActions(maximizingPlayer)

        expectiEval = 0
        totalActions = len(legalActions)
        if not totalActions:
            return 0
        for action in legalActions:
            if maximizingPlayer == (gameState.getNumAgents() - 1):
                currentExpected = float(
                    self.max_palyer(gameState.generateSuccessor(maximizingPlayer, action), depth + 1, 0)) / float(
                    totalActions)
            else:
                currentExpected = float(
                    self.ecpecti_player(gameState.generateSuccessor(maximizingPlayer, action), depth,
                                        maximizingPlayer + 1)) / float(totalActions)
            expectiEval += currentExpected
        return expectiEval

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        bestAction = None
        bestScore = float('-inf')
        legalActions = gameState.getLegalActions(0)
        for action in legalActions:
            score = self.ecpecti_player(gameState.generateSuccessor(0, action), 0, 1)
            if score > bestScore:
                bestScore = score
                bestAction = action
        return bestAction


class BetterMCTSAgent(MultiAgentSearchAgent):
    """
        Our improved MCTS Search Agent Class Implementation
    """
    def __init__(self, noOfIterations=100, depth=50):
        self.iterations = noOfIterations  # Choose the number of iterations
        self.depth = depth

    def getUCTValue(self, q, n, N, c):
        return q / n + c * sqrt(math.log(N) / n)  # Returns the UCT value of the node

    def getAction(self, gameState):
        if not gameState.getLegalActions(0):
            return Directions.STOP
        t0 = MCTSTreeNode(gameState, None, None)  # Create an MCTS root Node
        for _ in range(self.iterations):
            t1 = self.treePolicy(t0)  # Selection and Expansion
            delta = self.improvedPolicy(t1.state)  # Simulation
            self.backUpData(t1, delta)  # Back-propagation
        bestChildAction = self.bestChildAction(t0)  # Choose the best child among all the children
        if bestChildAction not in gameState.getLegalActions(0):
            return random.choice(gameState.getLegalActions(0))
        if bestChildAction is Directions.STOP:
            bestChildAction = self.goodChildAction(t0.state)
        return bestChildAction

    def treePolicy(self, node):
        while (not node.state.isWin()) and (not node.state.isLose()):
            if not node.isFullyExpanded:
                return self.expandNode(node)  # Expand the Node
            else:
                node = self.bestChild(node, 4)  # Pick the best child if fully expanded
        return node

    def expandNode(self, node):
        randomChildAction = random.choice(node.legalActions)
        node.legalActions.remove(randomChildAction)  # Choose a random legal action that has not been used yet
        if len(node.legalActions) == 0:
            node.isFullyExpanded = True
        newState = node.state.generateSuccessor(0, randomChildAction)
        newChildNode = MCTSTreeNode(newState, node, randomChildAction)
        node.childStates.append(newChildNode)  # Append the child node into childStates
        return newChildNode

    # Simulation policy
    def improvedPolicy(self, state):
        noofAgents = state.getNumAgents()
        isTerminalState = False
        it = 0
        while not isTerminalState:
            for i in range(noofAgents):
                it += 1
                isTerminalState = (
                    state.isWin() or
                    state.isLose() or
                    it > self.depth  # Limit the depth to remain within computational budget
                )
                if isTerminalState:
                    break
                if i > 0:  # Simulate ghost actions
                    randomChildAction = random.choice(state.getLegalActions(i))
                    state = state.generateSuccessor(i, randomChildAction)
                if i == 0:  # Simulate Pacman action
                    childAction = self.goodChildAction(state)
                    state = state.generateSuccessor(i, childAction)

        return self.getStateScore(state)

    # Back-propagates reward.
    def backUpData(self, node, delta):
        while node is not None:
            node.noofTimesVisited += 1
            node.reward += delta
            node = node.parent

    # Returns the best immediate child
    def bestChild(self, node, c):
        maxUCTValue = float('-inf')
        bestChild = None
        for child in node.childStates:
            uctValue = self.getUCTValue(child.reward, child.noOfTimesVisited, node.noOfTimesVisited, c)
            if uctValue > maxUCTValue:
                maxUCTValue = uctValue
                bestChild = child
        return bestChild

    # Chooses the best child Action which has best average reward value
    def bestChildAction(self, node):
        maxUCTValue = float('-inf')
        bestAction = None
        for child in node.childStates:
            uctValue = self.getUCTValue(child.reward, child.noOfTimesVisited, node.noOfTimesVisited, 0)
            if uctValue > maxUCTValue:
                maxUCTValue = uctValue
                bestAction = child.action
        return bestAction

    # Chooses the best child action to take in the simulation.
    def goodChildAction(self, state):
        legalMoves = state.getLegalActions(0)

        # Choose one of the best actions
        scores = [self.evaluationFunction(state, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)  # Pick randomly among the best

        return legalMoves[chosenIndex]

    # Score evaluation function for a given state and action.
    def evaluationFunction(self, currentGameState, action):
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        currentFood = currentGameState.getFood()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()

        score = 0
        # de-incentive 'Stop' action
        if action == 'Stop':
            return -100
        # food score
        for x in range(len(newFood[:])):
            for y in range(len(newFood[0][:])):
                # check with currentFood instead of newFood since new state might have the food eaten.
                if currentFood[x][y]:
                    foodDistance = util.manhattanDistance(newPos, (x, y))
                    # if new position has food
                    if foodDistance == 0:
                        score += 1
                    else:
                        # as pacman gets closer to food, increase score
                        score += 1 / (foodDistance * foodDistance)
        # increase score, as number of food decreases
        score /= 1 + successorGameState.getNumFood()  # add one to prevent divide by zero error.
        # capsule score
        for capsule in successorGameState.getCapsules():
            capsuleDistance = util.manhattanDistance(newPos, capsule)
            if capsuleDistance == 0:
                score += 1
            else:
                # as pacman gets closer to capsule, increase score
                score += 1 / capsuleDistance
        # ghost score
        for ghost in newGhostStates:
            scaredTimer = ghost.scaredTimer
            ghostDistance = util.manhattanDistance(newPos, ghost.getPosition())
            if scaredTimer > 0:
                # incentive for pacman to catch scared ghost.
                score += 1 / (1 + ghostDistance * ghostDistance)  # add one to prevent divide by zero error.
            else:
                # decrease score as pacman is catchable by ghost.
                if ghostDistance < 2:
                    score -= 100

        return score

    # Score evaluation function for a given state. Gets the "terminal" utility value after the depth limit.
    def getStateScore(self, state):
        # Food heuristic
        foods = state.getFood()  # get the food positions
        pacman_pos = state.getPacmanPosition()
        foodDist = []
        for food in foods.asList():
            foodDist.append(1 / math.pow(manhattanDistance(food, pacman_pos), 2))
        score = max(foodDist) if len(foodDist) > 0 else 0

        numOfFoodLeft = state.getNumFood()

        score = score + (50 / (1 + numOfFoodLeft))

        # Ghost heuristic
        newGhostStates = state.getGhostStates()

        for ghost in newGhostStates:
            scaredTimer = ghost.scaredTimer
            ghostDistance = util.manhattanDistance(pacman_pos, ghost.getPosition())
            if scaredTimer > 0:
                # incentive for pacman to catch scared ghost.
                score += 2 / math.pow((1 + ghostDistance), 2)  # add one to prevent divide by zero error.
            else:
                if ghostDistance < 2:
                    score = score - 1

        # Add state heuristic with the state utility
        return score + state.getScore()


class MCTSTreeNode:
    """
        MCTS Tree Node class
    """
    def __init__(self, state, parent, action):
        self.state = state
        self.legalActions = state.getLegalActions(0)
        self.childStates = []
        self.parent = parent
        self.noOfTimesVisited = 0
        self.reward = 0.0
        self.isFullyExpanded = False
        self.action = action


class MCTSAgent(MultiAgentSearchAgent):
    """
        Our MCTS Search Agent Class Implementation
    """

    def __init__(self, noOfIterations=100, depth=50):
        self.iterations = noOfIterations  # Choose the number of iterations
        self.depth = depth

    def getUCTValue(self, q, n, N, c):
        return (q / n) + c * sqrt(math.log(N) / n)  # Returns the UCT value of the node

    def getAction(self, gameState):
        if not gameState.getLegalActions(0):
            return Directions.STOP
        t0 = MCTSTreeNode(gameState, None, None)  # Create an MCTS root Node
        for _ in range(self.iterations):
            t1 = self.treePolicy(t0)  # Selection and Expansion
            delta = self.defaultPolicy(t1.state)  # Simulation
            self.backUpData(t1, delta)  # Back-propagation
        bestChildAction = self.bestChildAction(t0)  # Choose the best child among all the children
        if bestChildAction not in gameState.getLegalActions(0):
            return random.choice(gameState.getLegalActions(0))
        return bestChildAction

    def treePolicy(self, node):
        while not self.isTerminalState(node.state):
            if not node.isFullyExpanded:
                return self.expandNode(node)  # Expand the Node
            else:
                node = self.bestChild(node, 4)  # Pick the best child if fully expanded
        return node

    def isTerminalState(self, state):
        return state.isWin() or state.isLose()

    def expandNode(self, node):
        randomChildAction = random.choice(node.legalActions)  # Choose a random legal action that has not been used yet.
        node.legalActions.remove(randomChildAction)
        if len(node.legalActions) == 0:
            node.isFullyExpanded = True
        newState = node.state.generateSuccessor(0, randomChildAction)
        newChildNode = MCTSTreeNode(newState, node, randomChildAction)
        node.childStates.append(newChildNode)  # Append the child node into childStates
        return newChildNode

    # Simulation policy
    def defaultPolicy(self, state):
        isTerminalState = False
        it = 0
        while not isTerminalState:
            it = it + 1
            isTerminalState = state.isWin() or state.isLose() or it > self.depth
            if isTerminalState:
                break
            randomChildAction = random.choice(state.getLegalActions(0))  # Simulate using random action selection
            state = state.generateSuccessor(0, randomChildAction)
        score = self.getStateScore(state)
        return score

    # Back-propagates reward.
    def backUpData(self, node, delta):
        while node is not None:
            node.noofTimesVisited += 1
            node.reward += delta
            node = node.parent

    # Returns the best immediate child
    def bestChild(self, node, c):
        maxUCTValue = float('-inf')
        bestChild = None
        for child in node.childStates:
            uctValue = self.getUCTValue(child.reward, child.noOfTimesVisited, node.noOfTimesVisited, c)
            if uctValue > maxUCTValue:
                maxUCTValue = uctValue
                bestChild = child
        return bestChild

    # Chooses the best child Action which has best average reward value
    def bestChildAction(self, node):
        maxUCTValue = float('-inf')
        bestAction = None
        for child in node.childStates:
            uctValue = self.getUCTValue(child.reward, child.noOfTimesVisited, node.noOfTimesVisited, 0)
            if uctValue > maxUCTValue:
                maxUCTValue = uctValue
                bestAction = child.action
        return bestAction

    # Score evaluation function for a given state. Gets the "terminal" utility value after the depth limit.
    def getStateScore(self, state):
        score = 0
        if state.isWin():
            score += 1000
        if state.isLose():
            score -= 1000
        score += state.getScore()
        return score
