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
    score_match = re.search(r"Score: (-?\d+)", output.split('\n')[0])

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


def runSmallEnvs(numberOfEnvs=5):
    itrIndex = 0
    smallLayoutsLength = len(smallLayouts)
    while itrIndex <= numberOfEnvs:
        smallLayout = smallLayouts[itrIndex % smallLayoutsLength]
        if itrIndex == numberOfEnvs:
            break
        runScript(smallLayout,'small')
        itrIndex += 1

def runSmallEnvis(startRange, endRange):
    for i in range(startRange, endRange + 1):
        layoutName = '/small/small' + str(i) + '.lay'
        runScript(layoutName,'small')

def runMediumEnvs(startRange, endRange):
    for i in range(startRange, endRange + 1):
        layoutName = '/medium/medium' + str(i) + '.lay'
        runScript(layoutName,'medium')


def runLargeEnvs(startRange, endRange):
    for i in range(startRange, endRange + 1):
        layoutName = '/big/big' + str(i) + '.lay'
        runScript(layoutName,'large')


def runScript( layout,size):
    arg = ['-l', layout]
    if size =='small':
        timeout = 1*60
    elif size == 'medium':
        timeout = 2*60
    else:
        timeout = 3*60
    arg += ['-c']
    arg += ['--timeout',str(timeout)]
    args1 = ['-p', 'MCTSAgent'] + arg  # Replace with correct agent
    args2 = ['-p', 'BetterMCTSAgent'] + arg  # Replace with correct agent
    args3 = ['-p', 'AlphaBetaAgent'] + arg  # Replace with correct agent
    arge4 = ['-p','ExpectimaxAgent'] + arg
    environments.append(arg)
    scores1.append(execute_program(args1))
    scores2.append(execute_program(args2))
    scores3.append(execute_program(args3))
    scores4.append(execute_program(arge4))
    print("Environment: ", environments)
    print("Scores: ", scores1, scores2, scores3,scores4)


def runTTest():
    print("Environment: ", environments)
    print("Scores: ", scores1, scores2, scores3)

    print("Agent 1 normality test")
    normalityTest(scores1)
    print("Agent 2 normality test")
    normalityTest(scores2)
    print("Agent 3 normality test")
    normalityTest(scores3)

    t_statistic1, p_value1 = stats.ttest_rel(scores1, scores3)
    t_statistic2, p_value2 = stats.ttest_rel(scores2, scores3)

    # Define significance level (alpha)
    alphatTest = 0.05

    # Determine whether to reject or accept the null hypothesis
    print("------t-Test Agent 1 vs Agent 3------")
    if p_value1 < alphatTest:
        print("Reject the null hypothesis: There is a significant difference between the means")
    else:
        print("Accept the null hypothesis: There is no significant difference between the means")

    print("------t-Test Agent 2 vs Agent 3------")
    if p_value2 < alphatTest:
        print("Reject the null hypothesis: There is a significant difference between the means")
    else:
        print("Accept the null hypothesis: There is no significant difference between the means")

    # Print t-statistic and p-value
    print("t-statistic:", t_statistic1, t_statistic2)
    print("p-value:", p_value1, p_value2)


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
runSmallEnvis(1,30)
runMediumEnvs(1, 30)
runLargeEnvs(1, 30)

print("----------Final Results----------")
runTTest()
print("Environment: ", environments)
print("Scores: ", scores1, scores2, scores3,scores4)