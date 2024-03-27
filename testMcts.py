import re
import subprocess
import scipy.stats as stats
import sys
import os

"""
    TODO: add timeout if game takes too long.
"""

noOfSamples = 30  # change to 30 at least
scores1 = [[]]
scores2 = [[]]
scores3 = [[]]
environments = []

# Mazes
layouts = [
    # 'trickyClassic',
    # 'trappedClassic',
    'testClassic',
    # 'smallClassic',
    # 'powerClassic',
    'originalClassic',
    # 'openClassic',
    # 'minimaxClassic',
    # 'mediumClassic',
    # 'contestClassic',
    # 'capsuleClassic'
]

numberOfGhosts = [
    '2', '3', '4'
]


# Function to execute the external program with different parameters
def execute_program(args):
    command = ['python', 'pacman.py', '--frameTime', '0', '-q'] + args
    print("command: ", command)
    result = subprocess.run(command, capture_output=True, text=True)
    output = result.stdout.strip()
    print(output)
    score_match = re.search(r'Score: (-?\d+)', output.split('\n')[0])

    if score_match:
        score = float(score_match.group(1))
        return score

    print("No score found.")
    return None


def normalityTest(data):
    # Perform Shapiro-Wilk test
    statistic, p_value = stats.shapiro(data)

    # Print the test statistic and p-value
    print("Shapiro-Wilk Test:")
    print("Statistic:", statistic)
    print("p-value:", p_value)

    # Interpret the result
    alpha = 0.05
    if p_value > alpha:
        print("Sample looks Gaussian (fail to reject H0)")
    else:
        print("Sample does not look Gaussian (reject H0)")


def runScript():
    # Reflex Agent, GreedyAgent, LeftTurnAgent
    i = 0
    for layout in layouts:
        for ghost in numberOfGhosts:
            arg = ['-k', ghost, '-l', layout]
            args1 = ['-p', 'MCTSAgent'] + arg
            args2 = ['-p', 'BetterMCTSAgent'] + arg
            args3 = ['-p', 'LeftTurnAgent'] + arg
            environments.insert(i, arg)
            scores1.insert(i, [])
            scores2.insert(i, [])
            scores3.insert(i, [])
            for j in range(noOfSamples):
                scores1[i].append(execute_program(args1))
                scores2[i].append(execute_program(args2))
                scores3[i].append(execute_program(args3))
            i += 1

    for i in range(len(environments)):
        print("Environment: ", i, environments[i])
        print("Scores: ", i, scores1[i], scores2[i], scores3[i])

        print("Agent 1 normality test")
        normalityTest(scores1[i])
        print("Agent 2 normality test")
        normalityTest(scores2[i])
        print("Agent 3 normality test")
        normalityTest(scores3[i])

        t_statistic1, p_value1 = stats.ttest_rel(scores1[i], scores3[i])
        t_statistic2, p_value2 = stats.ttest_rel(scores2[i], scores3[i])

        # Define significance level (alpha)
        alphatTest = 0.05

        # Determine whether to reject or accept the null hypothesis
        if p_value1 < alphatTest:
            print("Reject the null hypothesis: There is a significant difference between the means")
        else:
            print("Accept the null hypothesis: There is no significant difference between the means")

        # Print t-statistic and p-value
        print("t-statistic:", t_statistic1, t_statistic2)
        print("p-value:", p_value1, p_value2)


def runAndSaveOutputToFile():
    # Define the directory name
    directory_name = "output"

    # Create the directory if it doesn't exist
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
    # Save the current sys.stdout for later use
    original_stdout = sys.stdout

    # Define the file path where you want to save the output
    output_file = "output/output1.txt"

    # Open the file in write mode, which will clear any existing content
    with open(output_file, "w") as f:
        # Redirect sys.stdout to the file
        sys.stdout = f

        runScript()

    # Reset sys.stdout to its original value
    sys.stdout = original_stdout

    print("Console output has been saved to", output_file)

runAndSaveOutputToFile()