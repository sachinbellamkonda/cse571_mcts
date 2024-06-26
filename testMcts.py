import random
import re
import subprocess
import sys

import scipy.stats as stats

scores1 = []
scores2 = []
scores3 = []
scores4 = []
environments = []

# Layouts
smallLayouts = [
    # 'trickyClassic',
    # 'trappedClassic',
    'testClassic',
    'smallClassic',
    # 'powerClassic',
    # 'originalClassic',
    # 'openClassic',
    'minimaxClassic',
    # 'mediumClassic',
    # 'contestClassic',
    # 'capsuleClassic'
]

mediumLayouts = []
largeLayouts = []


# Function to execute the external program with different parameters
def execute_program(args):
    command = ['python', 'pacman.py', '--frameTime', '0', '-q'] + args
    print("command: ", command)
    result = subprocess.run(command, capture_output=True, text=True)
    output = result.stdout.strip()
    print(output)
    score_match = re.search(r"Score: (-?\d+)", output.split('\n')[1])

    if score_match:
        score = float(score_match.group(1))
        return score

    print("No score found.")
    return None


def runSmallEnvs(numberOfEnvs=5):
    itrIndex = 0
    smallLayoutsLength = len(smallLayouts)
    while itrIndex <= numberOfEnvs:
        smallLayout = smallLayouts[itrIndex % smallLayoutsLength]
        if itrIndex == numberOfEnvs:
            break
        runScript(smallLayout, 'small')
        itrIndex += 1


def runSmallEnvis(startRange, endRange):
    for i in range(startRange, endRange + 1):
        layoutName = '/small/small' + str(i) + '.lay'
        runScript(layoutName, 'small')


def runMediumEnvs(startRange, endRange):
    for i in range(startRange, endRange + 1):
        layoutName = '/medium/medium' + str(i) + '.lay'
        runScript(layoutName, 'medium')


def runLargeEnvs(startRange, endRange):
    for i in range(startRange, endRange + 1):
        layoutName = '/large/large' + str(i) + '.lay'
        runScript(layoutName, 'large')


def runScript(layout, size):
    arg = ['-l', layout]
    if size == 'small':
        timeout = 1 * 60
    elif size == 'medium':
        timeout = 2 * 60
    else:
        timeout = 3 * 60
    arg += ['-c']
    arg += ['--timeout', str(timeout)]
    args1 = ['-p', 'MCTSAgent'] + arg  # Replace with correct agent
    args2 = ['-p', 'BetterMCTSAgent'] + arg  # Replace with correct agent
    args3 = ['-p', 'AlphaBetaAgent'] + arg  # Replace with correct agent
    arge4 = ['-p', 'ExpectimaxAgent'] + arg
    environments.append(arg)
    scores1.append(execute_program(args1))
    scores2.append(execute_program(args2))
    scores3.append(execute_program(args3))
    scores4.append(execute_program(arge4))
    print("Environment: ", environments)
    print("Scores: ", scores1, scores2, scores3, scores4)


# Not used anywhere
def saveOutputToFile(func, fileName):
    output = None
    # Save the current sys.stdout for later use
    original_stdout = sys.stdout

    # Define the file path where you want to save the output
    output_file = f"output/{fileName}.txt"

    # Open the file in write mode, which will clear any existing content
    with open(output_file, "w") as f:
        # Redirect sys.stdout to the file
        sys.stdout = f

        output = func()

    # Reset sys.stdout to its original value
    sys.stdout = original_stdout

    print("Console output has been saved to", output_file)
    return output


runSmallEnvs()
runSmallEnvis(1, 30)
runMediumEnvs(1, 30)
runLargeEnvs(1, 30)
