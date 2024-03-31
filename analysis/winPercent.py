output = """
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', 'testClassic', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 530
Average Score: 530.0
Scores:        530.0
Win Rate:      1/1 (1.00)
Record:        Win
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', 'testClassic', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 542
Average Score: 542.0
Scores:        542.0
Win Rate:      1/1 (1.00)
Record:        Win
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', 'testClassic', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 482
Average Score: 482.0
Scores:        482.0
Win Rate:      1/1 (1.00)
Record:        Win
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', 'testClassic', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 520
Average Score: 520.0
Scores:        520.0
Win Rate:      1/1 (1.00)
Record:        Win
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60']]
Scores:  [530.0] [542.0] [482.0] [520.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', 'smallClassic', '-c', '--timeout', '60']
Pacman died! Score: -147
Average Score: -147.0
Scores:        -147.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', 'smallClassic', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 1501
Average Score: 1501.0
Scores:        1501.0
Win Rate:      1/1 (1.00)
Record:        Win
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', 'smallClassic', '-c', '--timeout', '60']
Pacman died! Score: -220
Average Score: -220.0
Scores:        -220.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', 'smallClassic', '-c', '--timeout', '60']
Pacman died! Score: -426
Average Score: -426.0
Scores:        -426.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60']]
Scores:  [530.0, -147.0] [542.0, 1501.0] [482.0, -220.0] [520.0, -426.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', 'minimaxClassic', '-c', '--timeout', '60']
Pacman died! Score: -492
Average Score: -492.0
Scores:        -492.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', 'minimaxClassic', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 516
Average Score: 516.0
Scores:        516.0
Win Rate:      1/1 (1.00)
Record:        Win
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', 'minimaxClassic', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 516
Average Score: 516.0
Scores:        516.0
Win Rate:      1/1 (1.00)
Record:        Win
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', 'minimaxClassic', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 516
Average Score: 516.0
Scores:        516.0
Win Rate:      1/1 (1.00)
Record:        Win
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60']]
Scores:  [530.0, -147.0, -492.0] [542.0, 1501.0, 516.0] [482.0, -220.0, 516.0] [520.0, -426.0, 516.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', 'testClassic', '-c', '--timeout', '60']
Pacman died! Score: -518
Average Score: -518.0
Scores:        -518.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', 'testClassic', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 560
Average Score: 560.0
Scores:        560.0
Win Rate:      1/1 (1.00)
Record:        Win
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', 'testClassic', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 516
Average Score: 516.0
Scores:        516.0
Win Rate:      1/1 (1.00)
Record:        Win
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', 'testClassic', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 508
Average Score: 508.0
Scores:        508.0
Win Rate:      1/1 (1.00)
Record:        Win
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60']]
Scores:  [530.0, -147.0, -492.0, -518.0] [542.0, 1501.0, 516.0, 560.0] [482.0, -220.0, 516.0, 516.0] [520.0, -426.0, 516.0, 508.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', 'smallClassic', '-c', '--timeout', '60']
Pacman died! Score: -375
Average Score: -375.0
Scores:        -375.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', 'smallClassic', '-c', '--timeout', '60']
Pacman died! Score: -339
Average Score: -339.0
Scores:        -339.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', 'smallClassic', '-c', '--timeout', '60']
Pacman died! Score: -188
Average Score: -188.0
Scores:        -188.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', 'smallClassic', '-c', '--timeout', '60']
Pacman died! Score: -137
Average Score: -137.0
Scores:        -137.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0] [542.0, 1501.0, 516.0, 560.0, -339.0] [482.0, -220.0, 516.0, 516.0, -188.0] [520.0, -426.0, 516.0, 508.0, -137.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/small/small1.lay', '-c', '--timeout', '60']
Pacman died! Score: -460
Average Score: -460.0
Scores:        -460.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/small/small1.lay', '-c', '--timeout', '60']
Pacman died! Score: -395
Average Score: -395.0
Scores:        -395.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/small/small1.lay', '-c', '--timeout', '60']
Pacman died! Score: -464
Average Score: -464.0
Scores:        -464.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/small/small1.lay', '-c', '--timeout', '60']
Pacman died! Score: -583
Average Score: -583.0
Scores:        -583.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/small/small2.lay', '-c', '--timeout', '60']
Pacman died! Score: 249
Average Score: 249.0
Scores:        249.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/small/small2.lay', '-c', '--timeout', '60']
Pacman died! Score: -478
Average Score: -478.0
Scores:        -478.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/small/small2.lay', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 1619
Average Score: 1619.0
Scores:        1619.0
Win Rate:      1/1 (1.00)
Record:        Win
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/small/small2.lay', '-c', '--timeout', '60']
Pacman died! Score: -220
Average Score: -220.0
Scores:        -220.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/small/small3.lay', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 750
Average Score: 750.0
Scores:        750.0
Win Rate:      1/1 (1.00)
Record:        Win
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/small/small3.lay', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 828
Average Score: 828.0
Scores:        828.0
Win Rate:      1/1 (1.00)
Record:        Win
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/small/small3.lay', '-c', '--timeout', '60']
Pacman crashed
Average Score: 0.0
Scores:        0.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/small/small3.lay', '-c', '--timeout', '60']
Pacman crashed
Average Score: 0.0
Scores:        0.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/small/small4.lay', '-c', '--timeout', '60']
Pacman died! Score: -429
Average Score: -429.0
Scores:        -429.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/small/small4.lay', '-c', '--timeout', '60']
Pacman died! Score: -405
Average Score: -405.0
Scores:        -405.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/small/small4.lay', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 661
Average Score: 661.0
Scores:        661.0
Win Rate:      1/1 (1.00)
Record:        Win
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/small/small4.lay', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 651
Average Score: 651.0
Scores:        651.0
Win Rate:      1/1 (1.00)
Record:        Win
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/small/small5.lay', '-c', '--timeout', '60']
Pacman died! Score: -423
Average Score: -423.0
Scores:        -423.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/small/small5.lay', '-c', '--timeout', '60']
Pacman died! Score: -492
Average Score: -492.0
Scores:        -492.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/small/small5.lay', '-c', '--timeout', '60']
Pacman died! Score: -492
Average Score: -492.0
Scores:        -492.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/small/small5.lay', '-c', '--timeout', '60']
Pacman died! Score: -576
Average Score: -576.0
Scores:        -576.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/small/small6.lay', '-c', '--timeout', '60']
Pacman died! Score: 81
Average Score: 81.0
Scores:        81.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/small/small6.lay', '-c', '--timeout', '60']
Pacman died! Score: -440
Average Score: -440.0
Scores:        -440.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/small/small6.lay', '-c', '--timeout', '60']
Pacman died! Score: -513
Average Score: -513.0
Scores:        -513.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/small/small6.lay', '-c', '--timeout', '60']
Pacman died! Score: -438
Average Score: -438.0
Scores:        -438.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/small/small7.lay', '-c', '--timeout', '60']
Pacman died! Score: 78
Average Score: 78.0
Scores:        78.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/small/small7.lay', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 1472
Average Score: 1472.0
Scores:        1472.0
Win Rate:      1/1 (1.00)
Record:        Win
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/small/small7.lay', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 1729
Average Score: 1729.0
Scores:        1729.0
Win Rate:      1/1 (1.00)
Record:        Win
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/small/small7.lay', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 1800
Average Score: 1800.0
Scores:        1800.0
Win Rate:      1/1 (1.00)
Record:        Win
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/small/small8.lay', '-c', '--timeout', '60']
Pacman died! Score: -491
Average Score: -491.0
Scores:        -491.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/small/small8.lay', '-c', '--timeout', '60']
Pacman died! Score: -261
Average Score: -261.0
Scores:        -261.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/small/small8.lay', '-c', '--timeout', '60']
Pacman died! Score: -491
Average Score: -491.0
Scores:        -491.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/small/small8.lay', '-c', '--timeout', '60']
Pacman died! Score: -1617
Average Score: -1617.0
Scores:        -1617.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/small/small9.lay', '-c', '--timeout', '60']
Pacman died! Score: -462
Average Score: -462.0
Scores:        -462.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/small/small9.lay', '-c', '--timeout', '60']
Pacman died! Score: -425
Average Score: -425.0
Scores:        -425.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/small/small9.lay', '-c', '--timeout', '60']
Pacman died! Score: -457
Average Score: -457.0
Scores:        -457.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/small/small9.lay', '-c', '--timeout', '60']
Pacman died! Score: -499
Average Score: -499.0
Scores:        -499.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/small/small10.lay', '-c', '--timeout', '60']
Pacman died! Score: 200
Average Score: 200.0
Scores:        200.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/small/small10.lay', '-c', '--timeout', '60']
Pacman died! Score: -487
Average Score: -487.0
Scores:        -487.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/small/small10.lay', '-c', '--timeout', '60']
Pacman died! Score: -473
Average Score: -473.0
Scores:        -473.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/small/small10.lay', '-c', '--timeout', '60']
Pacman died! Score: -451
Average Score: -451.0
Scores:        -451.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/small/small11.lay', '-c', '--timeout', '60']
Pacman died! Score: -492
Average Score: -492.0
Scores:        -492.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/small/small11.lay', '-c', '--timeout', '60']
Pacman died! Score: -458
Average Score: -458.0
Scores:        -458.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/small/small11.lay', '-c', '--timeout', '60']
Pacman died! Score: -439
Average Score: -439.0
Scores:        -439.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/small/small11.lay', '-c', '--timeout', '60']
Pacman died! Score: -490
Average Score: -490.0
Scores:        -490.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/small/small12.lay', '-c', '--timeout', '60']
Pacman died! Score: 321
Average Score: 321.0
Scores:        321.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/small/small12.lay', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 1722
Average Score: 1722.0
Scores:        1722.0
Win Rate:      1/1 (1.00)
Record:        Win
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/small/small12.lay', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 415
Average Score: 415.0
Scores:        415.0
Win Rate:      1/1 (1.00)
Record:        Win
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/small/small12.lay', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 778
Average Score: 778.0
Scores:        778.0
Win Rate:      1/1 (1.00)
Record:        Win
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/small/small13.lay', '-c', '--timeout', '60']
Pacman died! Score: -473
Average Score: -473.0
Scores:        -473.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/small/small13.lay', '-c', '--timeout', '60']
Pacman died! Score: -482
Average Score: -482.0
Scores:        -482.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/small/small13.lay', '-c', '--timeout', '60']
Pacman died! Score: -461
Average Score: -461.0
Scores:        -461.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/small/small13.lay', '-c', '--timeout', '60']
Pacman died! Score: -438
Average Score: -438.0
Scores:        -438.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/small/small14.lay', '-c', '--timeout', '60']
Pacman died! Score: -419
Average Score: -419.0
Scores:        -419.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/small/small14.lay', '-c', '--timeout', '60']
Pacman died! Score: 293
Average Score: 293.0
Scores:        293.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/small/small14.lay', '-c', '--timeout', '60']
Pacman died! Score: -109
Average Score: -109.0
Scores:        -109.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/small/small14.lay', '-c', '--timeout', '60']
Pacman died! Score: 66
Average Score: 66.0
Scores:        66.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/small/small15.lay', '-c', '--timeout', '60']
Pacman died! Score: -224
Average Score: -224.0
Scores:        -224.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/small/small15.lay', '-c', '--timeout', '60']
Pacman died! Score: 234
Average Score: 234.0
Scores:        234.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/small/small15.lay', '-c', '--timeout', '60']
Pacman crashed
Average Score: -25814.0
Scores:        -25814.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/small/small15.lay', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 1582
Average Score: 1582.0
Scores:        1582.0
Win Rate:      1/1 (1.00)
Record:        Win
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/small/small16.lay', '-c', '--timeout', '60']
Pacman died! Score: -245
Average Score: -245.0
Scores:        -245.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/small/small16.lay', '-c', '--timeout', '60']
Pacman died! Score: -48
Average Score: -48.0
Scores:        -48.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/small/small16.lay', '-c', '--timeout', '60']
Pacman died! Score: -459
Average Score: -459.0
Scores:        -459.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/small/small16.lay', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 766
Average Score: 766.0
Scores:        766.0
Win Rate:      1/1 (1.00)
Record:        Win
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/small/small17.lay', '-c', '--timeout', '60']
Pacman crashed
Average Score: -628.0
Scores:        -628.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/small/small17.lay', '-c', '--timeout', '60']
Pacman crashed
Average Score: -377.0
Scores:        -377.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/small/small17.lay', '-c', '--timeout', '60']
Pacman crashed
Average Score: -45017.0
Scores:        -45017.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/small/small17.lay', '-c', '--timeout', '60']
Pacman crashed
Average Score: -46483.0
Scores:        -46483.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/small/small18.lay', '-c', '--timeout', '60']
Pacman died! Score: -482
Average Score: -482.0
Scores:        -482.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/small/small18.lay', '-c', '--timeout', '60']
Pacman died! Score: -427
Average Score: -427.0
Scores:        -427.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/small/small18.lay', '-c', '--timeout', '60']
Pacman died! Score: -429
Average Score: -429.0
Scores:        -429.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/small/small18.lay', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 609
Average Score: 609.0
Scores:        609.0
Win Rate:      1/1 (1.00)
Record:        Win
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/small/small19.lay', '-c', '--timeout', '60']
Pacman died! Score: -359
Average Score: -359.0
Scores:        -359.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/small/small19.lay', '-c', '--timeout', '60']
Pacman died! Score: 76
Average Score: 76.0
Scores:        76.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/small/small19.lay', '-c', '--timeout', '60']
Pacman died! Score: -457
Average Score: -457.0
Scores:        -457.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/small/small19.lay', '-c', '--timeout', '60']
Pacman died! Score: -908
Average Score: -908.0
Scores:        -908.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/small/small20.lay', '-c', '--timeout', '60']
Pacman died! Score: -137
Average Score: -137.0
Scores:        -137.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/small/small20.lay', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 1098
Average Score: 1098.0
Scores:        1098.0
Win Rate:      1/1 (1.00)
Record:        Win
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/small/small20.lay', '-c', '--timeout', '60']
Pacman emerges victorious! Score: -604
Average Score: -604.0
Scores:        -604.0
Win Rate:      1/1 (1.00)
Record:        Win
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/small/small20.lay', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 332
Average Score: 332.0
Scores:        332.0
Win Rate:      1/1 (1.00)
Record:        Win
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/small/small21.lay', '-c', '--timeout', '60']
Pacman died! Score: 101
Average Score: 101.0
Scores:        101.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/small/small21.lay', '-c', '--timeout', '60']
Pacman died! Score: 477
Average Score: 477.0
Scores:        477.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/small/small21.lay', '-c', '--timeout', '60']
Pacman died! Score: -650
Average Score: -650.0
Scores:        -650.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/small/small21.lay', '-c', '--timeout', '60']
Pacman died! Score: -70
Average Score: -70.0
Scores:        -70.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/small/small22.lay', '-c', '--timeout', '60']
Pacman died! Score: -90
Average Score: -90.0
Scores:        -90.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/small/small22.lay', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 1275
Average Score: 1275.0
Scores:        1275.0
Win Rate:      1/1 (1.00)
Record:        Win
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/small/small22.lay', '-c', '--timeout', '60']
Pacman died! Score: -436
Average Score: -436.0
Scores:        -436.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/small/small22.lay', '-c', '--timeout', '60']
Pacman died! Score: -333
Average Score: -333.0
Scores:        -333.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/small/small23.lay', '-c', '--timeout', '60']
Pacman died! Score: -471
Average Score: -471.0
Scores:        -471.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/small/small23.lay', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 776
Average Score: 776.0
Scores:        776.0
Win Rate:      1/1 (1.00)
Record:        Win
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/small/small23.lay', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 581
Average Score: 581.0
Scores:        581.0
Win Rate:      1/1 (1.00)
Record:        Win
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/small/small23.lay', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 773
Average Score: 773.0
Scores:        773.0
Win Rate:      1/1 (1.00)
Record:        Win
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/small/small24.lay', '-c', '--timeout', '60']
Pacman died! Score: -6
Average Score: -6.0
Scores:        -6.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/small/small24.lay', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 1074
Average Score: 1074.0
Scores:        1074.0
Win Rate:      1/1 (1.00)
Record:        Win
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/small/small24.lay', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 1253
Average Score: 1253.0
Scores:        1253.0
Win Rate:      1/1 (1.00)
Record:        Win
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/small/small24.lay', '-c', '--timeout', '60']
Pacman died! Score: 239
Average Score: 239.0
Scores:        239.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60'], ['-l', '/small/small24.lay', '-c', '--timeout', '60']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0, -6.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0, 1074.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0, 1253.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0, 239.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/small/small25.lay', '-c', '--timeout', '60']
Pacman died! Score: -478
Average Score: -478.0
Scores:        -478.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/small/small25.lay', '-c', '--timeout', '60']
Pacman died! Score: -455
Average Score: -455.0
Scores:        -455.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/small/small25.lay', '-c', '--timeout', '60']
Pacman died! Score: -411
Average Score: -411.0
Scores:        -411.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/small/small25.lay', '-c', '--timeout', '60']
Pacman died! Score: -443
Average Score: -443.0
Scores:        -443.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60'], ['-l', '/small/small24.lay', '-c', '--timeout', '60'], ['-l', '/small/small25.lay', '-c', '--timeout', '60']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0, -6.0, -478.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0, 1074.0, -455.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0, 1253.0, -411.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0, 239.0, -443.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/small/small26.lay', '-c', '--timeout', '60']
Pacman died! Score: -437
Average Score: -437.0
Scores:        -437.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/small/small26.lay', '-c', '--timeout', '60']
Pacman died! Score: -371
Average Score: -371.0
Scores:        -371.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/small/small26.lay', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 782
Average Score: 782.0
Scores:        782.0
Win Rate:      1/1 (1.00)
Record:        Win
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/small/small26.lay', '-c', '--timeout', '60']
Pacman emerges victorious! Score: -94
Average Score: -94.0
Scores:        -94.0
Win Rate:      1/1 (1.00)
Record:        Win
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60'], ['-l', '/small/small24.lay', '-c', '--timeout', '60'], ['-l', '/small/small25.lay', '-c', '--timeout', '60'], ['-l', '/small/small26.lay', '-c', '--timeout', '60']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0, -6.0, -478.0, -437.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0, 1074.0, -455.0, -371.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0, 1253.0, -411.0, 782.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0, 239.0, -443.0, -94.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/small/small27.lay', '-c', '--timeout', '60']
Pacman died! Score: 21
Average Score: 21.0
Scores:        21.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/small/small27.lay', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 1087
Average Score: 1087.0
Scores:        1087.0
Win Rate:      1/1 (1.00)
Record:        Win
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/small/small27.lay', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 851
Average Score: 851.0
Scores:        851.0
Win Rate:      1/1 (1.00)
Record:        Win
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/small/small27.lay', '-c', '--timeout', '60']
Pacman crashed
Average Score: -28346.0
Scores:        -28346.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60'], ['-l', '/small/small24.lay', '-c', '--timeout', '60'], ['-l', '/small/small25.lay', '-c', '--timeout', '60'], ['-l', '/small/small26.lay', '-c', '--timeout', '60'], ['-l', '/small/small27.lay', '-c', '--timeout', '60']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0, -6.0, -478.0, -437.0, 21.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0, 1074.0, -455.0, -371.0, 1087.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0, 1253.0, -411.0, 782.0, 851.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0, 239.0, -443.0, -94.0, -28346.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/small/small28.lay', '-c', '--timeout', '60']
Pacman died! Score: -266
Average Score: -266.0
Scores:        -266.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/small/small28.lay', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 747
Average Score: 747.0
Scores:        747.0
Win Rate:      1/1 (1.00)
Record:        Win
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/small/small28.lay', '-c', '--timeout', '60']
Pacman died! Score: -332
Average Score: -332.0
Scores:        -332.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/small/small28.lay', '-c', '--timeout', '60']
Pacman crashed
Average Score: -368.0
Scores:        -368.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60'], ['-l', '/small/small24.lay', '-c', '--timeout', '60'], ['-l', '/small/small25.lay', '-c', '--timeout', '60'], ['-l', '/small/small26.lay', '-c', '--timeout', '60'], ['-l', '/small/small27.lay', '-c', '--timeout', '60'], ['-l', '/small/small28.lay', '-c', '--timeout', '60']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0, -6.0, -478.0, -437.0, 21.0, -266.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0, 1074.0, -455.0, -371.0, 1087.0, 747.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0, 1253.0, -411.0, 782.0, 851.0, -332.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0, 239.0, -443.0, -94.0, -28346.0, -368.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/small/small29.lay', '-c', '--timeout', '60']
Pacman died! Score: -264
Average Score: -264.0
Scores:        -264.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/small/small29.lay', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 1430
Average Score: 1430.0
Scores:        1430.0
Win Rate:      1/1 (1.00)
Record:        Win
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/small/small29.lay', '-c', '--timeout', '60']
Pacman died! Score: -187
Average Score: -187.0
Scores:        -187.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/small/small29.lay', '-c', '--timeout', '60']
Pacman emerges victorious! Score: 1349
Average Score: 1349.0
Scores:        1349.0
Win Rate:      1/1 (1.00)
Record:        Win
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60'], ['-l', '/small/small24.lay', '-c', '--timeout', '60'], ['-l', '/small/small25.lay', '-c', '--timeout', '60'], ['-l', '/small/small26.lay', '-c', '--timeout', '60'], ['-l', '/small/small27.lay', '-c', '--timeout', '60'], ['-l', '/small/small28.lay', '-c', '--timeout', '60'], ['-l', '/small/small29.lay', '-c', '--timeout', '60']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0, -6.0, -478.0, -437.0, 21.0, -266.0, -264.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0, 1074.0, -455.0, -371.0, 1087.0, 747.0, 1430.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0, 1253.0, -411.0, 782.0, 851.0, -332.0, -187.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0, 239.0, -443.0, -94.0, -28346.0, -368.0, 1349.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/small/small30.lay', '-c', '--timeout', '60']
Pacman died! Score: -515
Average Score: -515.0
Scores:        -515.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/small/small30.lay', '-c', '--timeout', '60']
Pacman died! Score: -86
Average Score: -86.0
Scores:        -86.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/small/small30.lay', '-c', '--timeout', '60']
Pacman died! Score: -617
Average Score: -617.0
Scores:        -617.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/small/small30.lay', '-c', '--timeout', '60']
Pacman died! Score: -503
Average Score: -503.0
Scores:        -503.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60'], ['-l', '/small/small24.lay', '-c', '--timeout', '60'], ['-l', '/small/small25.lay', '-c', '--timeout', '60'], ['-l', '/small/small26.lay', '-c', '--timeout', '60'], ['-l', '/small/small27.lay', '-c', '--timeout', '60'], ['-l', '/small/small28.lay', '-c', '--timeout', '60'], ['-l', '/small/small29.lay', '-c', '--timeout', '60'], ['-l', '/small/small30.lay', '-c', '--timeout', '60']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0, -6.0, -478.0, -437.0, 21.0, -266.0, -264.0, -515.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0, 1074.0, -455.0, -371.0, 1087.0, 747.0, 1430.0, -86.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0, 1253.0, -411.0, 782.0, 851.0, -332.0, -187.0, -617.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0, 239.0, -443.0, -94.0, -28346.0, -368.0, 1349.0, -503.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/medium/medium1.lay', '-c', '--timeout', '120']
Pacman died! Score: -212
Average Score: -212.0
Scores:        -212.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/medium/medium1.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: 962.0
Scores:        962.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/medium/medium1.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: -41006.0
Scores:        -41006.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/medium/medium1.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: -40200.0
Scores:        -40200.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60'], ['-l', '/small/small24.lay', '-c', '--timeout', '60'], ['-l', '/small/small25.lay', '-c', '--timeout', '60'], ['-l', '/small/small26.lay', '-c', '--timeout', '60'], ['-l', '/small/small27.lay', '-c', '--timeout', '60'], ['-l', '/small/small28.lay', '-c', '--timeout', '60'], ['-l', '/small/small29.lay', '-c', '--timeout', '60'], ['-l', '/small/small30.lay', '-c', '--timeout', '60'], ['-l', '/medium/medium1.lay', '-c', '--timeout', '120']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0, -6.0, -478.0, -437.0, 21.0, -266.0, -264.0, -515.0, -212.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0, 1074.0, -455.0, -371.0, 1087.0, 747.0, 1430.0, -86.0, 962.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0, 1253.0, -411.0, 782.0, 851.0, -332.0, -187.0, -617.0, -41006.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0, 239.0, -443.0, -94.0, -28346.0, -368.0, 1349.0, -503.0, -40200.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/medium/medium2.lay', '-c', '--timeout', '120']
Pacman emerges victorious! Score: 796
Average Score: 796.0
Scores:        796.0
Win Rate:      1/1 (1.00)
Record:        Win
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/medium/medium2.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: 493.0
Scores:        493.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/medium/medium2.lay', '-c', '--timeout', '120']
Pacman died! Score: -22
Average Score: -22.0
Scores:        -22.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/medium/medium2.lay', '-c', '--timeout', '120']
Pacman died! Score: -448
Average Score: -448.0
Scores:        -448.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60'], ['-l', '/small/small24.lay', '-c', '--timeout', '60'], ['-l', '/small/small25.lay', '-c', '--timeout', '60'], ['-l', '/small/small26.lay', '-c', '--timeout', '60'], ['-l', '/small/small27.lay', '-c', '--timeout', '60'], ['-l', '/small/small28.lay', '-c', '--timeout', '60'], ['-l', '/small/small29.lay', '-c', '--timeout', '60'], ['-l', '/small/small30.lay', '-c', '--timeout', '60'], ['-l', '/medium/medium1.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium2.lay', '-c', '--timeout', '120']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0, -6.0, -478.0, -437.0, 21.0, -266.0, -264.0, -515.0, -212.0, 796.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0, 1074.0, -455.0, -371.0, 1087.0, 747.0, 1430.0, -86.0, 962.0, 493.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0, 1253.0, -411.0, 782.0, 851.0, -332.0, -187.0, -617.0, -41006.0, -22.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0, 239.0, -443.0, -94.0, -28346.0, -368.0, 1349.0, -503.0, -40200.0, -448.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/medium/medium3.lay', '-c', '--timeout', '120']
Pacman died! Score: 81
Average Score: 81.0
Scores:        81.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/medium/medium3.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: 570.0
Scores:        570.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/medium/medium3.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: -44651.0
Scores:        -44651.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/medium/medium3.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: -46285.0
Scores:        -46285.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60'], ['-l', '/small/small24.lay', '-c', '--timeout', '60'], ['-l', '/small/small25.lay', '-c', '--timeout', '60'], ['-l', '/small/small26.lay', '-c', '--timeout', '60'], ['-l', '/small/small27.lay', '-c', '--timeout', '60'], ['-l', '/small/small28.lay', '-c', '--timeout', '60'], ['-l', '/small/small29.lay', '-c', '--timeout', '60'], ['-l', '/small/small30.lay', '-c', '--timeout', '60'], ['-l', '/medium/medium1.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium2.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium3.lay', '-c', '--timeout', '120']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0, -6.0, -478.0, -437.0, 21.0, -266.0, -264.0, -515.0, -212.0, 796.0, 81.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0, 1074.0, -455.0, -371.0, 1087.0, 747.0, 1430.0, -86.0, 962.0, 493.0, 570.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0, 1253.0, -411.0, 782.0, 851.0, -332.0, -187.0, -617.0, -41006.0, -22.0, -44651.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0, 239.0, -443.0, -94.0, -28346.0, -368.0, 1349.0, -503.0, -40200.0, -448.0, -46285.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/medium/medium4.lay', '-c', '--timeout', '120']
Pacman died! Score: 226
Average Score: 226.0
Scores:        226.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/medium/medium4.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: 1273.0
Scores:        1273.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/medium/medium4.lay', '-c', '--timeout', '120']
Pacman died! Score: -359
Average Score: -359.0
Scores:        -359.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/medium/medium4.lay', '-c', '--timeout', '120']
Pacman died! Score: -778
Average Score: -778.0
Scores:        -778.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60'], ['-l', '/small/small24.lay', '-c', '--timeout', '60'], ['-l', '/small/small25.lay', '-c', '--timeout', '60'], ['-l', '/small/small26.lay', '-c', '--timeout', '60'], ['-l', '/small/small27.lay', '-c', '--timeout', '60'], ['-l', '/small/small28.lay', '-c', '--timeout', '60'], ['-l', '/small/small29.lay', '-c', '--timeout', '60'], ['-l', '/small/small30.lay', '-c', '--timeout', '60'], ['-l', '/medium/medium1.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium2.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium3.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium4.lay', '-c', '--timeout', '120']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0, -6.0, -478.0, -437.0, 21.0, -266.0, -264.0, -515.0, -212.0, 796.0, 81.0, 226.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0, 1074.0, -455.0, -371.0, 1087.0, 747.0, 1430.0, -86.0, 962.0, 493.0, 570.0, 1273.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0, 1253.0, -411.0, 782.0, 851.0, -332.0, -187.0, -617.0, -41006.0, -22.0, -44651.0, -359.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0, 239.0, -443.0, -94.0, -28346.0, -368.0, 1349.0, -503.0, -40200.0, -448.0, -46285.0, -778.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/medium/medium5.lay', '-c', '--timeout', '120']
Pacman died! Score: -482
Average Score: -482.0
Scores:        -482.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/medium/medium5.lay', '-c', '--timeout', '120']
Pacman died! Score: -406
Average Score: -406.0
Scores:        -406.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/medium/medium5.lay', '-c', '--timeout', '120']
Pacman died! Score: -526
Average Score: -526.0
Scores:        -526.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/medium/medium5.lay', '-c', '--timeout', '120']
Pacman died! Score: -421
Average Score: -421.0
Scores:        -421.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60'], ['-l', '/small/small24.lay', '-c', '--timeout', '60'], ['-l', '/small/small25.lay', '-c', '--timeout', '60'], ['-l', '/small/small26.lay', '-c', '--timeout', '60'], ['-l', '/small/small27.lay', '-c', '--timeout', '60'], ['-l', '/small/small28.lay', '-c', '--timeout', '60'], ['-l', '/small/small29.lay', '-c', '--timeout', '60'], ['-l', '/small/small30.lay', '-c', '--timeout', '60'], ['-l', '/medium/medium1.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium2.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium3.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium4.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium5.lay', '-c', '--timeout', '120']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0, -6.0, -478.0, -437.0, 21.0, -266.0, -264.0, -515.0, -212.0, 796.0, 81.0, 226.0, -482.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0, 1074.0, -455.0, -371.0, 1087.0, 747.0, 1430.0, -86.0, 962.0, 493.0, 570.0, 1273.0, -406.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0, 1253.0, -411.0, 782.0, 851.0, -332.0, -187.0, -617.0, -41006.0, -22.0, -44651.0, -359.0, -526.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0, 239.0, -443.0, -94.0, -28346.0, -368.0, 1349.0, -503.0, -40200.0, -448.0, -46285.0, -778.0, -421.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/medium/medium6.lay', '-c', '--timeout', '120']
Pacman died! Score: -491
Average Score: -491.0
Scores:        -491.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/medium/medium6.lay', '-c', '--timeout', '120']
Pacman died! Score: 51
Average Score: 51.0
Scores:        51.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/medium/medium6.lay', '-c', '--timeout', '120']
Pacman died! Score: -313
Average Score: -313.0
Scores:        -313.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/medium/medium6.lay', '-c', '--timeout', '120']
Pacman died! Score: -403
Average Score: -403.0
Scores:        -403.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60'], ['-l', '/small/small24.lay', '-c', '--timeout', '60'], ['-l', '/small/small25.lay', '-c', '--timeout', '60'], ['-l', '/small/small26.lay', '-c', '--timeout', '60'], ['-l', '/small/small27.lay', '-c', '--timeout', '60'], ['-l', '/small/small28.lay', '-c', '--timeout', '60'], ['-l', '/small/small29.lay', '-c', '--timeout', '60'], ['-l', '/small/small30.lay', '-c', '--timeout', '60'], ['-l', '/medium/medium1.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium2.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium3.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium4.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium5.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium6.lay', '-c', '--timeout', '120']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0, -6.0, -478.0, -437.0, 21.0, -266.0, -264.0, -515.0, -212.0, 796.0, 81.0, 226.0, -482.0, -491.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0, 1074.0, -455.0, -371.0, 1087.0, 747.0, 1430.0, -86.0, 962.0, 493.0, 570.0, 1273.0, -406.0, 51.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0, 1253.0, -411.0, 782.0, 851.0, -332.0, -187.0, -617.0, -41006.0, -22.0, -44651.0, -359.0, -526.0, -313.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0, 239.0, -443.0, -94.0, -28346.0, -368.0, 1349.0, -503.0, -40200.0, -448.0, -46285.0, -778.0, -421.0, -403.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/medium/medium7.lay', '-c', '--timeout', '120']
Pacman died! Score: -149
Average Score: -149.0
Scores:        -149.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/medium/medium7.lay', '-c', '--timeout', '120']
Pacman died! Score: 751
Average Score: 751.0
Scores:        751.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/medium/medium7.lay', '-c', '--timeout', '120']
Pacman died! Score: -716
Average Score: -716.0
Scores:        -716.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/medium/medium7.lay', '-c', '--timeout', '120']
Pacman died! Score: -1328
Average Score: -1328.0
Scores:        -1328.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60'], ['-l', '/small/small24.lay', '-c', '--timeout', '60'], ['-l', '/small/small25.lay', '-c', '--timeout', '60'], ['-l', '/small/small26.lay', '-c', '--timeout', '60'], ['-l', '/small/small27.lay', '-c', '--timeout', '60'], ['-l', '/small/small28.lay', '-c', '--timeout', '60'], ['-l', '/small/small29.lay', '-c', '--timeout', '60'], ['-l', '/small/small30.lay', '-c', '--timeout', '60'], ['-l', '/medium/medium1.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium2.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium3.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium4.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium5.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium6.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium7.lay', '-c', '--timeout', '120']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0, -6.0, -478.0, -437.0, 21.0, -266.0, -264.0, -515.0, -212.0, 796.0, 81.0, 226.0, -482.0, -491.0, -149.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0, 1074.0, -455.0, -371.0, 1087.0, 747.0, 1430.0, -86.0, 962.0, 493.0, 570.0, 1273.0, -406.0, 51.0, 751.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0, 1253.0, -411.0, 782.0, 851.0, -332.0, -187.0, -617.0, -41006.0, -22.0, -44651.0, -359.0, -526.0, -313.0, -716.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0, 239.0, -443.0, -94.0, -28346.0, -368.0, 1349.0, -503.0, -40200.0, -448.0, -46285.0, -778.0, -421.0, -403.0, -1328.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/medium/medium8.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: -792.0
Scores:        -792.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/medium/medium8.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: -294.0
Scores:        -294.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/medium/medium8.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: -4139.0
Scores:        -4139.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/medium/medium8.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: -4147.0
Scores:        -4147.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60'], ['-l', '/small/small24.lay', '-c', '--timeout', '60'], ['-l', '/small/small25.lay', '-c', '--timeout', '60'], ['-l', '/small/small26.lay', '-c', '--timeout', '60'], ['-l', '/small/small27.lay', '-c', '--timeout', '60'], ['-l', '/small/small28.lay', '-c', '--timeout', '60'], ['-l', '/small/small29.lay', '-c', '--timeout', '60'], ['-l', '/small/small30.lay', '-c', '--timeout', '60'], ['-l', '/medium/medium1.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium2.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium3.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium4.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium5.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium6.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium7.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium8.lay', '-c', '--timeout', '120']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0, -6.0, -478.0, -437.0, 21.0, -266.0, -264.0, -515.0, -212.0, 796.0, 81.0, 226.0, -482.0, -491.0, -149.0, -792.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0, 1074.0, -455.0, -371.0, 1087.0, 747.0, 1430.0, -86.0, 962.0, 493.0, 570.0, 1273.0, -406.0, 51.0, 751.0, -294.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0, 1253.0, -411.0, 782.0, 851.0, -332.0, -187.0, -617.0, -41006.0, -22.0, -44651.0, -359.0, -526.0, -313.0, -716.0, -4139.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0, 239.0, -443.0, -94.0, -28346.0, -368.0, 1349.0, -503.0, -40200.0, -448.0, -46285.0, -778.0, -421.0, -403.0, -1328.0, -4147.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/medium/medium9.lay', '-c', '--timeout', '120']
Pacman died! Score: 326
Average Score: 326.0
Scores:        326.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/medium/medium9.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: 1090.0
Scores:        1090.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/medium/medium9.lay', '-c', '--timeout', '120']
Pacman died! Score: -562
Average Score: -562.0
Scores:        -562.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/medium/medium9.lay', '-c', '--timeout', '120']
Pacman died! Score: -858
Average Score: -858.0
Scores:        -858.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60'], ['-l', '/small/small24.lay', '-c', '--timeout', '60'], ['-l', '/small/small25.lay', '-c', '--timeout', '60'], ['-l', '/small/small26.lay', '-c', '--timeout', '60'], ['-l', '/small/small27.lay', '-c', '--timeout', '60'], ['-l', '/small/small28.lay', '-c', '--timeout', '60'], ['-l', '/small/small29.lay', '-c', '--timeout', '60'], ['-l', '/small/small30.lay', '-c', '--timeout', '60'], ['-l', '/medium/medium1.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium2.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium3.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium4.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium5.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium6.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium7.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium8.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium9.lay', '-c', '--timeout', '120']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0, -6.0, -478.0, -437.0, 21.0, -266.0, -264.0, -515.0, -212.0, 796.0, 81.0, 226.0, -482.0, -491.0, -149.0, -792.0, 326.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0, 1074.0, -455.0, -371.0, 1087.0, 747.0, 1430.0, -86.0, 962.0, 493.0, 570.0, 1273.0, -406.0, 51.0, 751.0, -294.0, 1090.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0, 1253.0, -411.0, 782.0, 851.0, -332.0, -187.0, -617.0, -41006.0, -22.0, -44651.0, -359.0, -526.0, -313.0, -716.0, -4139.0, -562.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0, 239.0, -443.0, -94.0, -28346.0, -368.0, 1349.0, -503.0, -40200.0, -448.0, -46285.0, -778.0, -421.0, -403.0, -1328.0, -4147.0, -858.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/medium/medium10.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: 1212.0
Scores:        1212.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/medium/medium10.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: 1111.0
Scores:        1111.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/medium/medium10.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: -2916.0
Scores:        -2916.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/medium/medium10.lay', '-c', '--timeout', '120']
Pacman died! Score: 112
Average Score: 112.0
Scores:        112.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60'], ['-l', '/small/small24.lay', '-c', '--timeout', '60'], ['-l', '/small/small25.lay', '-c', '--timeout', '60'], ['-l', '/small/small26.lay', '-c', '--timeout', '60'], ['-l', '/small/small27.lay', '-c', '--timeout', '60'], ['-l', '/small/small28.lay', '-c', '--timeout', '60'], ['-l', '/small/small29.lay', '-c', '--timeout', '60'], ['-l', '/small/small30.lay', '-c', '--timeout', '60'], ['-l', '/medium/medium1.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium2.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium3.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium4.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium5.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium6.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium7.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium8.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium9.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium10.lay', '-c', '--timeout', '120']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0, -6.0, -478.0, -437.0, 21.0, -266.0, -264.0, -515.0, -212.0, 796.0, 81.0, 226.0, -482.0, -491.0, -149.0, -792.0, 326.0, 1212.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0, 1074.0, -455.0, -371.0, 1087.0, 747.0, 1430.0, -86.0, 962.0, 493.0, 570.0, 1273.0, -406.0, 51.0, 751.0, -294.0, 1090.0, 1111.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0, 1253.0, -411.0, 782.0, 851.0, -332.0, -187.0, -617.0, -41006.0, -22.0, -44651.0, -359.0, -526.0, -313.0, -716.0, -4139.0, -562.0, -2916.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0, 239.0, -443.0, -94.0, -28346.0, -368.0, 1349.0, -503.0, -40200.0, -448.0, -46285.0, -778.0, -421.0, -403.0, -1328.0, -4147.0, -858.0, 112.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/medium/medium11.lay', '-c', '--timeout', '120']
Pacman died! Score: -491
Average Score: -491.0
Scores:        -491.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/medium/medium11.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: 1865.0
Scores:        1865.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/medium/medium11.lay', '-c', '--timeout', '120']
Pacman died! Score: -491
Average Score: -491.0
Scores:        -491.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/medium/medium11.lay', '-c', '--timeout', '120']
Pacman died! Score: -502
Average Score: -502.0
Scores:        -502.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60'], ['-l', '/small/small24.lay', '-c', '--timeout', '60'], ['-l', '/small/small25.lay', '-c', '--timeout', '60'], ['-l', '/small/small26.lay', '-c', '--timeout', '60'], ['-l', '/small/small27.lay', '-c', '--timeout', '60'], ['-l', '/small/small28.lay', '-c', '--timeout', '60'], ['-l', '/small/small29.lay', '-c', '--timeout', '60'], ['-l', '/small/small30.lay', '-c', '--timeout', '60'], ['-l', '/medium/medium1.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium2.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium3.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium4.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium5.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium6.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium7.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium8.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium9.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium10.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium11.lay', '-c', '--timeout', '120']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0, -6.0, -478.0, -437.0, 21.0, -266.0, -264.0, -515.0, -212.0, 796.0, 81.0, 226.0, -482.0, -491.0, -149.0, -792.0, 326.0, 1212.0, -491.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0, 1074.0, -455.0, -371.0, 1087.0, 747.0, 1430.0, -86.0, 962.0, 493.0, 570.0, 1273.0, -406.0, 51.0, 751.0, -294.0, 1090.0, 1111.0, 1865.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0, 1253.0, -411.0, 782.0, 851.0, -332.0, -187.0, -617.0, -41006.0, -22.0, -44651.0, -359.0, -526.0, -313.0, -716.0, -4139.0, -562.0, -2916.0, -491.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0, 239.0, -443.0, -94.0, -28346.0, -368.0, 1349.0, -503.0, -40200.0, -448.0, -46285.0, -778.0, -421.0, -403.0, -1328.0, -4147.0, -858.0, 112.0, -502.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/medium/medium12.lay', '-c', '--timeout', '120']
Pacman died! Score: 104
Average Score: 104.0
Scores:        104.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/medium/medium12.lay', '-c', '--timeout', '120']
Pacman died! Score: 654
Average Score: 654.0
Scores:        654.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/medium/medium12.lay', '-c', '--timeout', '120']
Pacman died! Score: -397
Average Score: -397.0
Scores:        -397.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/medium/medium12.lay', '-c', '--timeout', '120']
Pacman died! Score: 287
Average Score: 287.0
Scores:        287.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60'], ['-l', '/small/small24.lay', '-c', '--timeout', '60'], ['-l', '/small/small25.lay', '-c', '--timeout', '60'], ['-l', '/small/small26.lay', '-c', '--timeout', '60'], ['-l', '/small/small27.lay', '-c', '--timeout', '60'], ['-l', '/small/small28.lay', '-c', '--timeout', '60'], ['-l', '/small/small29.lay', '-c', '--timeout', '60'], ['-l', '/small/small30.lay', '-c', '--timeout', '60'], ['-l', '/medium/medium1.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium2.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium3.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium4.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium5.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium6.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium7.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium8.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium9.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium10.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium11.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium12.lay', '-c', '--timeout', '120']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0, -6.0, -478.0, -437.0, 21.0, -266.0, -264.0, -515.0, -212.0, 796.0, 81.0, 226.0, -482.0, -491.0, -149.0, -792.0, 326.0, 1212.0, -491.0, 104.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0, 1074.0, -455.0, -371.0, 1087.0, 747.0, 1430.0, -86.0, 962.0, 493.0, 570.0, 1273.0, -406.0, 51.0, 751.0, -294.0, 1090.0, 1111.0, 1865.0, 654.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0, 1253.0, -411.0, 782.0, 851.0, -332.0, -187.0, -617.0, -41006.0, -22.0, -44651.0, -359.0, -526.0, -313.0, -716.0, -4139.0, -562.0, -2916.0, -491.0, -397.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0, 239.0, -443.0, -94.0, -28346.0, -368.0, 1349.0, -503.0, -40200.0, -448.0, -46285.0, -778.0, -421.0, -403.0, -1328.0, -4147.0, -858.0, 112.0, -502.0, 287.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/medium/medium13.lay', '-c', '--timeout', '120']
Pacman emerges victorious! Score: 405
Average Score: 405.0
Scores:        405.0
Win Rate:      1/1 (1.00)
Record:        Win
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/medium/medium13.lay', '-c', '--timeout', '120']
Pacman emerges victorious! Score: 1060
Average Score: 1060.0
Scores:        1060.0
Win Rate:      1/1 (1.00)
Record:        Win
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/medium/medium13.lay', '-c', '--timeout', '120']
Pacman died! Score: -414
Average Score: -414.0
Scores:        -414.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/medium/medium13.lay', '-c', '--timeout', '120']
Pacman died! Score: -347
Average Score: -347.0
Scores:        -347.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60'], ['-l', '/small/small24.lay', '-c', '--timeout', '60'], ['-l', '/small/small25.lay', '-c', '--timeout', '60'], ['-l', '/small/small26.lay', '-c', '--timeout', '60'], ['-l', '/small/small27.lay', '-c', '--timeout', '60'], ['-l', '/small/small28.lay', '-c', '--timeout', '60'], ['-l', '/small/small29.lay', '-c', '--timeout', '60'], ['-l', '/small/small30.lay', '-c', '--timeout', '60'], ['-l', '/medium/medium1.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium2.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium3.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium4.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium5.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium6.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium7.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium8.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium9.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium10.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium11.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium12.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium13.lay', '-c', '--timeout', '120']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0, -6.0, -478.0, -437.0, 21.0, -266.0, -264.0, -515.0, -212.0, 796.0, 81.0, 226.0, -482.0, -491.0, -149.0, -792.0, 326.0, 1212.0, -491.0, 104.0, 405.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0, 1074.0, -455.0, -371.0, 1087.0, 747.0, 1430.0, -86.0, 962.0, 493.0, 570.0, 1273.0, -406.0, 51.0, 751.0, -294.0, 1090.0, 1111.0, 1865.0, 654.0, 1060.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0, 1253.0, -411.0, 782.0, 851.0, -332.0, -187.0, -617.0, -41006.0, -22.0, -44651.0, -359.0, -526.0, -313.0, -716.0, -4139.0, -562.0, -2916.0, -491.0, -397.0, -414.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0, 239.0, -443.0, -94.0, -28346.0, -368.0, 1349.0, -503.0, -40200.0, -448.0, -46285.0, -778.0, -421.0, -403.0, -1328.0, -4147.0, -858.0, 112.0, -502.0, 287.0, -347.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/medium/medium14.lay', '-c', '--timeout', '120']
Pacman died! Score: -125
Average Score: -125.0
Scores:        -125.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/medium/medium14.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: 1502.0
Scores:        1502.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/medium/medium14.lay', '-c', '--timeout', '120']
Pacman died! Score: 1097
Average Score: 1097.0
Scores:        1097.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/medium/medium14.lay', '-c', '--timeout', '120']
Pacman died! Score: -1084
Average Score: -1084.0
Scores:        -1084.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60'], ['-l', '/small/small24.lay', '-c', '--timeout', '60'], ['-l', '/small/small25.lay', '-c', '--timeout', '60'], ['-l', '/small/small26.lay', '-c', '--timeout', '60'], ['-l', '/small/small27.lay', '-c', '--timeout', '60'], ['-l', '/small/small28.lay', '-c', '--timeout', '60'], ['-l', '/small/small29.lay', '-c', '--timeout', '60'], ['-l', '/small/small30.lay', '-c', '--timeout', '60'], ['-l', '/medium/medium1.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium2.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium3.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium4.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium5.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium6.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium7.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium8.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium9.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium10.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium11.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium12.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium13.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium14.lay', '-c', '--timeout', '120']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0, -6.0, -478.0, -437.0, 21.0, -266.0, -264.0, -515.0, -212.0, 796.0, 81.0, 226.0, -482.0, -491.0, -149.0, -792.0, 326.0, 1212.0, -491.0, 104.0, 405.0, -125.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0, 1074.0, -455.0, -371.0, 1087.0, 747.0, 1430.0, -86.0, 962.0, 493.0, 570.0, 1273.0, -406.0, 51.0, 751.0, -294.0, 1090.0, 1111.0, 1865.0, 654.0, 1060.0, 1502.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0, 1253.0, -411.0, 782.0, 851.0, -332.0, -187.0, -617.0, -41006.0, -22.0, -44651.0, -359.0, -526.0, -313.0, -716.0, -4139.0, -562.0, -2916.0, -491.0, -397.0, -414.0, 1097.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0, 239.0, -443.0, -94.0, -28346.0, -368.0, 1349.0, -503.0, -40200.0, -448.0, -46285.0, -778.0, -421.0, -403.0, -1328.0, -4147.0, -858.0, 112.0, -502.0, 287.0, -347.0, -1084.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/medium/medium15.lay', '-c', '--timeout', '120']
Pacman died! Score: -454
Average Score: -454.0
Scores:        -454.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/medium/medium15.lay', '-c', '--timeout', '120']
Pacman emerges victorious! Score: 1190
Average Score: 1190.0
Scores:        1190.0
Win Rate:      1/1 (1.00)
Record:        Win
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/medium/medium15.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: -40135.0
Scores:        -40135.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/medium/medium15.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: -37773.0
Scores:        -37773.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60'], ['-l', '/small/small24.lay', '-c', '--timeout', '60'], ['-l', '/small/small25.lay', '-c', '--timeout', '60'], ['-l', '/small/small26.lay', '-c', '--timeout', '60'], ['-l', '/small/small27.lay', '-c', '--timeout', '60'], ['-l', '/small/small28.lay', '-c', '--timeout', '60'], ['-l', '/small/small29.lay', '-c', '--timeout', '60'], ['-l', '/small/small30.lay', '-c', '--timeout', '60'], ['-l', '/medium/medium1.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium2.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium3.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium4.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium5.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium6.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium7.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium8.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium9.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium10.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium11.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium12.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium13.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium14.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium15.lay', '-c', '--timeout', '120']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0, -6.0, -478.0, -437.0, 21.0, -266.0, -264.0, -515.0, -212.0, 796.0, 81.0, 226.0, -482.0, -491.0, -149.0, -792.0, 326.0, 1212.0, -491.0, 104.0, 405.0, -125.0, -454.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0, 1074.0, -455.0, -371.0, 1087.0, 747.0, 1430.0, -86.0, 962.0, 493.0, 570.0, 1273.0, -406.0, 51.0, 751.0, -294.0, 1090.0, 1111.0, 1865.0, 654.0, 1060.0, 1502.0, 1190.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0, 1253.0, -411.0, 782.0, 851.0, -332.0, -187.0, -617.0, -41006.0, -22.0, -44651.0, -359.0, -526.0, -313.0, -716.0, -4139.0, -562.0, -2916.0, -491.0, -397.0, -414.0, 1097.0, -40135.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0, 239.0, -443.0, -94.0, -28346.0, -368.0, 1349.0, -503.0, -40200.0, -448.0, -46285.0, -778.0, -421.0, -403.0, -1328.0, -4147.0, -858.0, 112.0, -502.0, 287.0, -347.0, -1084.0, -37773.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/medium/medium16.lay', '-c', '--timeout', '120']
Pacman died! Score: -49
Average Score: -49.0
Scores:        -49.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/medium/medium16.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: 1306.0
Scores:        1306.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/medium/medium16.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: -666.0
Scores:        -666.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/medium/medium16.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: 504.0
Scores:        504.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60'], ['-l', '/small/small24.lay', '-c', '--timeout', '60'], ['-l', '/small/small25.lay', '-c', '--timeout', '60'], ['-l', '/small/small26.lay', '-c', '--timeout', '60'], ['-l', '/small/small27.lay', '-c', '--timeout', '60'], ['-l', '/small/small28.lay', '-c', '--timeout', '60'], ['-l', '/small/small29.lay', '-c', '--timeout', '60'], ['-l', '/small/small30.lay', '-c', '--timeout', '60'], ['-l', '/medium/medium1.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium2.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium3.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium4.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium5.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium6.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium7.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium8.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium9.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium10.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium11.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium12.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium13.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium14.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium15.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium16.lay', '-c', '--timeout', '120']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0, -6.0, -478.0, -437.0, 21.0, -266.0, -264.0, -515.0, -212.0, 796.0, 81.0, 226.0, -482.0, -491.0, -149.0, -792.0, 326.0, 1212.0, -491.0, 104.0, 405.0, -125.0, -454.0, -49.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0, 1074.0, -455.0, -371.0, 1087.0, 747.0, 1430.0, -86.0, 962.0, 493.0, 570.0, 1273.0, -406.0, 51.0, 751.0, -294.0, 1090.0, 1111.0, 1865.0, 654.0, 1060.0, 1502.0, 1190.0, 1306.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0, 1253.0, -411.0, 782.0, 851.0, -332.0, -187.0, -617.0, -41006.0, -22.0, -44651.0, -359.0, -526.0, -313.0, -716.0, -4139.0, -562.0, -2916.0, -491.0, -397.0, -414.0, 1097.0, -40135.0, -666.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0, 239.0, -443.0, -94.0, -28346.0, -368.0, 1349.0, -503.0, -40200.0, -448.0, -46285.0, -778.0, -421.0, -403.0, -1328.0, -4147.0, -858.0, 112.0, -502.0, 287.0, -347.0, -1084.0, -37773.0, 504.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/medium/medium17.lay', '-c', '--timeout', '120']
Pacman died! Score: -368
Average Score: -368.0
Scores:        -368.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/medium/medium17.lay', '-c', '--timeout', '120']
Pacman died! Score: 180
Average Score: 180.0
Scores:        180.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/medium/medium17.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: -52680.0
Scores:        -52680.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/medium/medium17.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: -56854.0
Scores:        -56854.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60'], ['-l', '/small/small24.lay', '-c', '--timeout', '60'], ['-l', '/small/small25.lay', '-c', '--timeout', '60'], ['-l', '/small/small26.lay', '-c', '--timeout', '60'], ['-l', '/small/small27.lay', '-c', '--timeout', '60'], ['-l', '/small/small28.lay', '-c', '--timeout', '60'], ['-l', '/small/small29.lay', '-c', '--timeout', '60'], ['-l', '/small/small30.lay', '-c', '--timeout', '60'], ['-l', '/medium/medium1.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium2.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium3.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium4.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium5.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium6.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium7.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium8.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium9.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium10.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium11.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium12.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium13.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium14.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium15.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium16.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium17.lay', '-c', '--timeout', '120']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0, -6.0, -478.0, -437.0, 21.0, -266.0, -264.0, -515.0, -212.0, 796.0, 81.0, 226.0, -482.0, -491.0, -149.0, -792.0, 326.0, 1212.0, -491.0, 104.0, 405.0, -125.0, -454.0, -49.0, -368.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0, 1074.0, -455.0, -371.0, 1087.0, 747.0, 1430.0, -86.0, 962.0, 493.0, 570.0, 1273.0, -406.0, 51.0, 751.0, -294.0, 1090.0, 1111.0, 1865.0, 654.0, 1060.0, 1502.0, 1190.0, 1306.0, 180.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0, 1253.0, -411.0, 782.0, 851.0, -332.0, -187.0, -617.0, -41006.0, -22.0, -44651.0, -359.0, -526.0, -313.0, -716.0, -4139.0, -562.0, -2916.0, -491.0, -397.0, -414.0, 1097.0, -40135.0, -666.0, -52680.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0, 239.0, -443.0, -94.0, -28346.0, -368.0, 1349.0, -503.0, -40200.0, -448.0, -46285.0, -778.0, -421.0, -403.0, -1328.0, -4147.0, -858.0, 112.0, -502.0, 287.0, -347.0, -1084.0, -37773.0, 504.0, -56854.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/medium/medium18.lay', '-c', '--timeout', '120']
Pacman died! Score: -122
Average Score: -122.0
Scores:        -122.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/medium/medium18.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: 1603.0
Scores:        1603.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/medium/medium18.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: 284.0
Scores:        284.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/medium/medium18.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: 359.0
Scores:        359.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60'], ['-l', '/small/small24.lay', '-c', '--timeout', '60'], ['-l', '/small/small25.lay', '-c', '--timeout', '60'], ['-l', '/small/small26.lay', '-c', '--timeout', '60'], ['-l', '/small/small27.lay', '-c', '--timeout', '60'], ['-l', '/small/small28.lay', '-c', '--timeout', '60'], ['-l', '/small/small29.lay', '-c', '--timeout', '60'], ['-l', '/small/small30.lay', '-c', '--timeout', '60'], ['-l', '/medium/medium1.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium2.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium3.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium4.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium5.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium6.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium7.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium8.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium9.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium10.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium11.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium12.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium13.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium14.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium15.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium16.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium17.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium18.lay', '-c', '--timeout', '120']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0, -6.0, -478.0, -437.0, 21.0, -266.0, -264.0, -515.0, -212.0, 796.0, 81.0, 226.0, -482.0, -491.0, -149.0, -792.0, 326.0, 1212.0, -491.0, 104.0, 405.0, -125.0, -454.0, -49.0, -368.0, -122.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0, 1074.0, -455.0, -371.0, 1087.0, 747.0, 1430.0, -86.0, 962.0, 493.0, 570.0, 1273.0, -406.0, 51.0, 751.0, -294.0, 1090.0, 1111.0, 1865.0, 654.0, 1060.0, 1502.0, 1190.0, 1306.0, 180.0, 1603.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0, 1253.0, -411.0, 782.0, 851.0, -332.0, -187.0, -617.0, -41006.0, -22.0, -44651.0, -359.0, -526.0, -313.0, -716.0, -4139.0, -562.0, -2916.0, -491.0, -397.0, -414.0, 1097.0, -40135.0, -666.0, -52680.0, 284.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0, 239.0, -443.0, -94.0, -28346.0, -368.0, 1349.0, -503.0, -40200.0, -448.0, -46285.0, -778.0, -421.0, -403.0, -1328.0, -4147.0, -858.0, 112.0, -502.0, 287.0, -347.0, -1084.0, -37773.0, 504.0, -56854.0, 359.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/medium/medium19.lay', '-c', '--timeout', '120']
Pacman died! Score: -524
Average Score: -524.0
Scores:        -524.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/medium/medium19.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: 477.0
Scores:        477.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/medium/medium19.lay', '-c', '--timeout', '120']
Pacman died! Score: -588
Average Score: -588.0
Scores:        -588.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/medium/medium19.lay', '-c', '--timeout', '120']
Pacman died! Score: 107
Average Score: 107.0
Scores:        107.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60'], ['-l', '/small/small24.lay', '-c', '--timeout', '60'], ['-l', '/small/small25.lay', '-c', '--timeout', '60'], ['-l', '/small/small26.lay', '-c', '--timeout', '60'], ['-l', '/small/small27.lay', '-c', '--timeout', '60'], ['-l', '/small/small28.lay', '-c', '--timeout', '60'], ['-l', '/small/small29.lay', '-c', '--timeout', '60'], ['-l', '/small/small30.lay', '-c', '--timeout', '60'], ['-l', '/medium/medium1.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium2.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium3.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium4.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium5.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium6.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium7.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium8.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium9.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium10.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium11.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium12.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium13.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium14.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium15.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium16.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium17.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium18.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium19.lay', '-c', '--timeout', '120']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0, -6.0, -478.0, -437.0, 21.0, -266.0, -264.0, -515.0, -212.0, 796.0, 81.0, 226.0, -482.0, -491.0, -149.0, -792.0, 326.0, 1212.0, -491.0, 104.0, 405.0, -125.0, -454.0, -49.0, -368.0, -122.0, -524.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0, 1074.0, -455.0, -371.0, 1087.0, 747.0, 1430.0, -86.0, 962.0, 493.0, 570.0, 1273.0, -406.0, 51.0, 751.0, -294.0, 1090.0, 1111.0, 1865.0, 654.0, 1060.0, 1502.0, 1190.0, 1306.0, 180.0, 1603.0, 477.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0, 1253.0, -411.0, 782.0, 851.0, -332.0, -187.0, -617.0, -41006.0, -22.0, -44651.0, -359.0, -526.0, -313.0, -716.0, -4139.0, -562.0, -2916.0, -491.0, -397.0, -414.0, 1097.0, -40135.0, -666.0, -52680.0, 284.0, -588.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0, 239.0, -443.0, -94.0, -28346.0, -368.0, 1349.0, -503.0, -40200.0, -448.0, -46285.0, -778.0, -421.0, -403.0, -1328.0, -4147.0, -858.0, 112.0, -502.0, 287.0, -347.0, -1084.0, -37773.0, 504.0, -56854.0, 359.0, 107.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/medium/medium20.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: -455.0
Scores:        -455.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/medium/medium20.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: 14.0
Scores:        14.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/medium/medium20.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: -79539.0
Scores:        -79539.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/medium/medium20.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: -82842.0
Scores:        -82842.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60'], ['-l', '/small/small24.lay', '-c', '--timeout', '60'], ['-l', '/small/small25.lay', '-c', '--timeout', '60'], ['-l', '/small/small26.lay', '-c', '--timeout', '60'], ['-l', '/small/small27.lay', '-c', '--timeout', '60'], ['-l', '/small/small28.lay', '-c', '--timeout', '60'], ['-l', '/small/small29.lay', '-c', '--timeout', '60'], ['-l', '/small/small30.lay', '-c', '--timeout', '60'], ['-l', '/medium/medium1.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium2.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium3.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium4.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium5.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium6.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium7.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium8.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium9.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium10.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium11.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium12.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium13.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium14.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium15.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium16.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium17.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium18.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium19.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium20.lay', '-c', '--timeout', '120']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0, -6.0, -478.0, -437.0, 21.0, -266.0, -264.0, -515.0, -212.0, 796.0, 81.0, 226.0, -482.0, -491.0, -149.0, -792.0, 326.0, 1212.0, -491.0, 104.0, 405.0, -125.0, -454.0, -49.0, -368.0, -122.0, -524.0, -455.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0, 1074.0, -455.0, -371.0, 1087.0, 747.0, 1430.0, -86.0, 962.0, 493.0, 570.0, 1273.0, -406.0, 51.0, 751.0, -294.0, 1090.0, 1111.0, 1865.0, 654.0, 1060.0, 1502.0, 1190.0, 1306.0, 180.0, 1603.0, 477.0, 14.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0, 1253.0, -411.0, 782.0, 851.0, -332.0, -187.0, -617.0, -41006.0, -22.0, -44651.0, -359.0, -526.0, -313.0, -716.0, -4139.0, -562.0, -2916.0, -491.0, -397.0, -414.0, 1097.0, -40135.0, -666.0, -52680.0, 284.0, -588.0, -79539.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0, 239.0, -443.0, -94.0, -28346.0, -368.0, 1349.0, -503.0, -40200.0, -448.0, -46285.0, -778.0, -421.0, -403.0, -1328.0, -4147.0, -858.0, 112.0, -502.0, 287.0, -347.0, -1084.0, -37773.0, 504.0, -56854.0, 359.0, 107.0, -82842.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/medium/medium21.lay', '-c', '--timeout', '120']
Pacman died! Score: -344
Average Score: -344.0
Scores:        -344.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/medium/medium21.lay', '-c', '--timeout', '120']
Pacman died! Score: 576
Average Score: 576.0
Scores:        576.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/medium/medium21.lay', '-c', '--timeout', '120']
Pacman died! Score: -407
Average Score: -407.0
Scores:        -407.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/medium/medium21.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: -3742.0
Scores:        -3742.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60'], ['-l', '/small/small24.lay', '-c', '--timeout', '60'], ['-l', '/small/small25.lay', '-c', '--timeout', '60'], ['-l', '/small/small26.lay', '-c', '--timeout', '60'], ['-l', '/small/small27.lay', '-c', '--timeout', '60'], ['-l', '/small/small28.lay', '-c', '--timeout', '60'], ['-l', '/small/small29.lay', '-c', '--timeout', '60'], ['-l', '/small/small30.lay', '-c', '--timeout', '60'], ['-l', '/medium/medium1.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium2.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium3.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium4.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium5.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium6.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium7.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium8.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium9.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium10.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium11.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium12.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium13.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium14.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium15.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium16.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium17.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium18.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium19.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium20.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium21.lay', '-c', '--timeout', '120']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0, -6.0, -478.0, -437.0, 21.0, -266.0, -264.0, -515.0, -212.0, 796.0, 81.0, 226.0, -482.0, -491.0, -149.0, -792.0, 326.0, 1212.0, -491.0, 104.0, 405.0, -125.0, -454.0, -49.0, -368.0, -122.0, -524.0, -455.0, -344.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0, 1074.0, -455.0, -371.0, 1087.0, 747.0, 1430.0, -86.0, 962.0, 493.0, 570.0, 1273.0, -406.0, 51.0, 751.0, -294.0, 1090.0, 1111.0, 1865.0, 654.0, 1060.0, 1502.0, 1190.0, 1306.0, 180.0, 1603.0, 477.0, 14.0, 576.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0, 1253.0, -411.0, 782.0, 851.0, -332.0, -187.0, -617.0, -41006.0, -22.0, -44651.0, -359.0, -526.0, -313.0, -716.0, -4139.0, -562.0, -2916.0, -491.0, -397.0, -414.0, 1097.0, -40135.0, -666.0, -52680.0, 284.0, -588.0, -79539.0, -407.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0, 239.0, -443.0, -94.0, -28346.0, -368.0, 1349.0, -503.0, -40200.0, -448.0, -46285.0, -778.0, -421.0, -403.0, -1328.0, -4147.0, -858.0, 112.0, -502.0, 287.0, -347.0, -1084.0, -37773.0, 504.0, -56854.0, 359.0, 107.0, -82842.0, -3742.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/medium/medium22.lay', '-c', '--timeout', '120']
Pacman died! Score: 44
Average Score: 44.0
Scores:        44.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/medium/medium22.lay', '-c', '--timeout', '120']
Pacman emerges victorious! Score: 3000  													
Average Score: 3000.0
Scores:        3000.0
Win Rate:      1/1 (1.00)
Record:        Win
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/medium/medium22.lay', '-c', '--timeout', '120']
Pacman died! Score: 846
Average Score: 846.0
Scores:        846.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/medium/medium22.lay', '-c', '--timeout', '120']
Pacman died! Score: -653
Average Score: -653.0
Scores:        -653.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60'], ['-l', '/small/small24.lay', '-c', '--timeout', '60'], ['-l', '/small/small25.lay', '-c', '--timeout', '60'], ['-l', '/small/small26.lay', '-c', '--timeout', '60'], ['-l', '/small/small27.lay', '-c', '--timeout', '60'], ['-l', '/small/small28.lay', '-c', '--timeout', '60'], ['-l', '/small/small29.lay', '-c', '--timeout', '60'], ['-l', '/small/small30.lay', '-c', '--timeout', '60'], ['-l', '/medium/medium1.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium2.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium3.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium4.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium5.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium6.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium7.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium8.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium9.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium10.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium11.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium12.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium13.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium14.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium15.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium16.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium17.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium18.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium19.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium20.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium21.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium22.lay', '-c', '--timeout', '120']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0, -6.0, -478.0, -437.0, 21.0, -266.0, -264.0, -515.0, -212.0, 796.0, 81.0, 226.0, -482.0, -491.0, -149.0, -792.0, 326.0, 1212.0, -491.0, 104.0, 405.0, -125.0, -454.0, -49.0, -368.0, -122.0, -524.0, -455.0, -344.0, 44.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0, 1074.0, -455.0, -371.0, 1087.0, 747.0, 1430.0, -86.0, 962.0, 493.0, 570.0, 1273.0, -406.0, 51.0, 751.0, -294.0, 1090.0, 1111.0, 1865.0, 654.0, 1060.0, 1502.0, 1190.0, 1306.0, 180.0, 1603.0, 477.0, 14.0, 576.0, 3000.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0, 1253.0, -411.0, 782.0, 851.0, -332.0, -187.0, -617.0, -41006.0, -22.0, -44651.0, -359.0, -526.0, -313.0, -716.0, -4139.0, -562.0, -2916.0, -491.0, -397.0, -414.0, 1097.0, -40135.0, -666.0, -52680.0, 284.0, -588.0, -79539.0, -407.0, 846.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0, 239.0, -443.0, -94.0, -28346.0, -368.0, 1349.0, -503.0, -40200.0, -448.0, -46285.0, -778.0, -421.0, -403.0, -1328.0, -4147.0, -858.0, 112.0, -502.0, 287.0, -347.0, -1084.0, -37773.0, 504.0, -56854.0, 359.0, 107.0, -82842.0, -3742.0, -653.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/medium/medium23.lay', '-c', '--timeout', '120']
Pacman died! Score: -273
Average Score: -273.0
Scores:        -273.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/medium/medium23.lay', '-c', '--timeout', '120']
Pacman died! Score: 295
Average Score: 295.0
Scores:        295.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/medium/medium23.lay', '-c', '--timeout', '120']
Pacman died! Score: -284
Average Score: -284.0
Scores:        -284.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/medium/medium23.lay', '-c', '--timeout', '120']
Pacman died! Score: -924
Average Score: -924.0
Scores:        -924.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60'], ['-l', '/small/small24.lay', '-c', '--timeout', '60'], ['-l', '/small/small25.lay', '-c', '--timeout', '60'], ['-l', '/small/small26.lay', '-c', '--timeout', '60'], ['-l', '/small/small27.lay', '-c', '--timeout', '60'], ['-l', '/small/small28.lay', '-c', '--timeout', '60'], ['-l', '/small/small29.lay', '-c', '--timeout', '60'], ['-l', '/small/small30.lay', '-c', '--timeout', '60'], ['-l', '/medium/medium1.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium2.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium3.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium4.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium5.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium6.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium7.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium8.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium9.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium10.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium11.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium12.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium13.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium14.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium15.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium16.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium17.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium18.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium19.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium20.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium21.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium22.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium23.lay', '-c', '--timeout', '120']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0, -6.0, -478.0, -437.0, 21.0, -266.0, -264.0, -515.0, -212.0, 796.0, 81.0, 226.0, -482.0, -491.0, -149.0, -792.0, 326.0, 1212.0, -491.0, 104.0, 405.0, -125.0, -454.0, -49.0, -368.0, -122.0, -524.0, -455.0, -344.0, 44.0, -273.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0, 1074.0, -455.0, -371.0, 1087.0, 747.0, 1430.0, -86.0, 962.0, 493.0, 570.0, 1273.0, -406.0, 51.0, 751.0, -294.0, 1090.0, 1111.0, 1865.0, 654.0, 1060.0, 1502.0, 1190.0, 1306.0, 180.0, 1603.0, 477.0, 14.0, 576.0, 3000.0, 295.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0, 1253.0, -411.0, 782.0, 851.0, -332.0, -187.0, -617.0, -41006.0, -22.0, -44651.0, -359.0, -526.0, -313.0, -716.0, -4139.0, -562.0, -2916.0, -491.0, -397.0, -414.0, 1097.0, -40135.0, -666.0, -52680.0, 284.0, -588.0, -79539.0, -407.0, 846.0, -284.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0, 239.0, -443.0, -94.0, -28346.0, -368.0, 1349.0, -503.0, -40200.0, -448.0, -46285.0, -778.0, -421.0, -403.0, -1328.0, -4147.0, -858.0, 112.0, -502.0, 287.0, -347.0, -1084.0, -37773.0, 504.0, -56854.0, 359.0, 107.0, -82842.0, -3742.0, -653.0, -924.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/medium/medium24.lay', '-c', '--timeout', '120']
Pacman died! Score: -93
Average Score: -93.0
Scores:        -93.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/medium/medium24.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: 1798.0
Scores:        1798.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/medium/medium24.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: -39.0
Scores:        -39.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/medium/medium24.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: 1258.0
Scores:        1258.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60'], ['-l', '/small/small24.lay', '-c', '--timeout', '60'], ['-l', '/small/small25.lay', '-c', '--timeout', '60'], ['-l', '/small/small26.lay', '-c', '--timeout', '60'], ['-l', '/small/small27.lay', '-c', '--timeout', '60'], ['-l', '/small/small28.lay', '-c', '--timeout', '60'], ['-l', '/small/small29.lay', '-c', '--timeout', '60'], ['-l', '/small/small30.lay', '-c', '--timeout', '60'], ['-l', '/medium/medium1.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium2.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium3.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium4.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium5.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium6.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium7.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium8.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium9.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium10.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium11.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium12.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium13.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium14.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium15.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium16.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium17.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium18.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium19.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium20.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium21.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium22.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium23.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium24.lay', '-c', '--timeout', '120']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0, -6.0, -478.0, -437.0, 21.0, -266.0, -264.0, -515.0, -212.0, 796.0, 81.0, 226.0, -482.0, -491.0, -149.0, -792.0, 326.0, 1212.0, -491.0, 104.0, 405.0, -125.0, -454.0, -49.0, -368.0, -122.0, -524.0, -455.0, -344.0, 44.0, -273.0, -93.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0, 1074.0, -455.0, -371.0, 1087.0, 747.0, 1430.0, -86.0, 962.0, 493.0, 570.0, 1273.0, -406.0, 51.0, 751.0, -294.0, 1090.0, 1111.0, 1865.0, 654.0, 1060.0, 1502.0, 1190.0, 1306.0, 180.0, 1603.0, 477.0, 14.0, 576.0, 3000.0, 295.0, 1798.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0, 1253.0, -411.0, 782.0, 851.0, -332.0, -187.0, -617.0, -41006.0, -22.0, -44651.0, -359.0, -526.0, -313.0, -716.0, -4139.0, -562.0, -2916.0, -491.0, -397.0, -414.0, 1097.0, -40135.0, -666.0, -52680.0, 284.0, -588.0, -79539.0, -407.0, 846.0, -284.0, -39.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0, 239.0, -443.0, -94.0, -28346.0, -368.0, 1349.0, -503.0, -40200.0, -448.0, -46285.0, -778.0, -421.0, -403.0, -1328.0, -4147.0, -858.0, 112.0, -502.0, 287.0, -347.0, -1084.0, -37773.0, 504.0, -56854.0, 359.0, 107.0, -82842.0, -3742.0, -653.0, -924.0, 1258.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/medium/medium25.lay', '-c', '--timeout', '120']
Pacman died! Score: 138
Average Score: 138.0
Scores:        138.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/medium/medium25.lay', '-c', '--timeout', '120']
Pacman died! Score: 1398
Average Score: 1398.0
Scores:        1398.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/medium/medium25.lay', '-c', '--timeout', '120']
Pacman died! Score: -742
Average Score: -742.0
Scores:        -742.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/medium/medium25.lay', '-c', '--timeout', '120']
Pacman died! Score: -297
Average Score: -297.0
Scores:        -297.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60'], ['-l', '/small/small24.lay', '-c', '--timeout', '60'], ['-l', '/small/small25.lay', '-c', '--timeout', '60'], ['-l', '/small/small26.lay', '-c', '--timeout', '60'], ['-l', '/small/small27.lay', '-c', '--timeout', '60'], ['-l', '/small/small28.lay', '-c', '--timeout', '60'], ['-l', '/small/small29.lay', '-c', '--timeout', '60'], ['-l', '/small/small30.lay', '-c', '--timeout', '60'], ['-l', '/medium/medium1.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium2.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium3.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium4.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium5.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium6.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium7.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium8.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium9.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium10.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium11.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium12.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium13.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium14.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium15.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium16.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium17.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium18.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium19.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium20.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium21.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium22.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium23.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium24.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium25.lay', '-c', '--timeout', '120']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0, -6.0, -478.0, -437.0, 21.0, -266.0, -264.0, -515.0, -212.0, 796.0, 81.0, 226.0, -482.0, -491.0, -149.0, -792.0, 326.0, 1212.0, -491.0, 104.0, 405.0, -125.0, -454.0, -49.0, -368.0, -122.0, -524.0, -455.0, -344.0, 44.0, -273.0, -93.0, 138.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0, 1074.0, -455.0, -371.0, 1087.0, 747.0, 1430.0, -86.0, 962.0, 493.0, 570.0, 1273.0, -406.0, 51.0, 751.0, -294.0, 1090.0, 1111.0, 1865.0, 654.0, 1060.0, 1502.0, 1190.0, 1306.0, 180.0, 1603.0, 477.0, 14.0, 576.0, 3000.0, 295.0, 1798.0, 1398.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0, 1253.0, -411.0, 782.0, 851.0, -332.0, -187.0, -617.0, -41006.0, -22.0, -44651.0, -359.0, -526.0, -313.0, -716.0, -4139.0, -562.0, -2916.0, -491.0, -397.0, -414.0, 1097.0, -40135.0, -666.0, -52680.0, 284.0, -588.0, -79539.0, -407.0, 846.0, -284.0, -39.0, -742.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0, 239.0, -443.0, -94.0, -28346.0, -368.0, 1349.0, -503.0, -40200.0, -448.0, -46285.0, -778.0, -421.0, -403.0, -1328.0, -4147.0, -858.0, 112.0, -502.0, 287.0, -347.0, -1084.0, -37773.0, 504.0, -56854.0, 359.0, 107.0, -82842.0, -3742.0, -653.0, -924.0, 1258.0, -297.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/medium/medium26.lay', '-c', '--timeout', '120']
Pacman died! Score: 26
Average Score: 26.0
Scores:        26.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/medium/medium26.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: 2381.0
Scores:        2381.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/medium/medium26.lay', '-c', '--timeout', '120']
Pacman died! Score: 816
Average Score: 816.0
Scores:        816.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/medium/medium26.lay', '-c', '--timeout', '120']
Pacman died! Score: -6061
Average Score: -6061.0
Scores:        -6061.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60'], ['-l', '/small/small24.lay', '-c', '--timeout', '60'], ['-l', '/small/small25.lay', '-c', '--timeout', '60'], ['-l', '/small/small26.lay', '-c', '--timeout', '60'], ['-l', '/small/small27.lay', '-c', '--timeout', '60'], ['-l', '/small/small28.lay', '-c', '--timeout', '60'], ['-l', '/small/small29.lay', '-c', '--timeout', '60'], ['-l', '/small/small30.lay', '-c', '--timeout', '60'], ['-l', '/medium/medium1.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium2.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium3.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium4.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium5.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium6.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium7.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium8.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium9.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium10.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium11.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium12.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium13.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium14.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium15.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium16.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium17.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium18.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium19.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium20.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium21.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium22.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium23.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium24.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium25.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium26.lay', '-c', '--timeout', '120']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0, -6.0, -478.0, -437.0, 21.0, -266.0, -264.0, -515.0, -212.0, 796.0, 81.0, 226.0, -482.0, -491.0, -149.0, -792.0, 326.0, 1212.0, -491.0, 104.0, 405.0, -125.0, -454.0, -49.0, -368.0, -122.0, -524.0, -455.0, -344.0, 44.0, -273.0, -93.0, 138.0, 26.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0, 1074.0, -455.0, -371.0, 1087.0, 747.0, 1430.0, -86.0, 962.0, 493.0, 570.0, 1273.0, -406.0, 51.0, 751.0, -294.0, 1090.0, 1111.0, 1865.0, 654.0, 1060.0, 1502.0, 1190.0, 1306.0, 180.0, 1603.0, 477.0, 14.0, 576.0, 3000.0, 295.0, 1798.0, 1398.0, 2381.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0, 1253.0, -411.0, 782.0, 851.0, -332.0, -187.0, -617.0, -41006.0, -22.0, -44651.0, -359.0, -526.0, -313.0, -716.0, -4139.0, -562.0, -2916.0, -491.0, -397.0, -414.0, 1097.0, -40135.0, -666.0, -52680.0, 284.0, -588.0, -79539.0, -407.0, 846.0, -284.0, -39.0, -742.0, 816.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0, 239.0, -443.0, -94.0, -28346.0, -368.0, 1349.0, -503.0, -40200.0, -448.0, -46285.0, -778.0, -421.0, -403.0, -1328.0, -4147.0, -858.0, 112.0, -502.0, 287.0, -347.0, -1084.0, -37773.0, 504.0, -56854.0, 359.0, 107.0, -82842.0, -3742.0, -653.0, -924.0, 1258.0, -297.0, -6061.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/medium/medium27.lay', '-c', '--timeout', '120']
Pacman died! Score: 534
Average Score: 534.0
Scores:        534.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/medium/medium27.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: 989.0
Scores:        989.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/medium/medium27.lay', '-c', '--timeout', '120']
Pacman died! Score: -121
Average Score: -121.0
Scores:        -121.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/medium/medium27.lay', '-c', '--timeout', '120']
Pacman died! Score: 985
Average Score: 985.0
Scores:        985.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60'], ['-l', '/small/small24.lay', '-c', '--timeout', '60'], ['-l', '/small/small25.lay', '-c', '--timeout', '60'], ['-l', '/small/small26.lay', '-c', '--timeout', '60'], ['-l', '/small/small27.lay', '-c', '--timeout', '60'], ['-l', '/small/small28.lay', '-c', '--timeout', '60'], ['-l', '/small/small29.lay', '-c', '--timeout', '60'], ['-l', '/small/small30.lay', '-c', '--timeout', '60'], ['-l', '/medium/medium1.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium2.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium3.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium4.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium5.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium6.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium7.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium8.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium9.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium10.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium11.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium12.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium13.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium14.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium15.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium16.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium17.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium18.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium19.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium20.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium21.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium22.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium23.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium24.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium25.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium26.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium27.lay', '-c', '--timeout', '120']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0, -6.0, -478.0, -437.0, 21.0, -266.0, -264.0, -515.0, -212.0, 796.0, 81.0, 226.0, -482.0, -491.0, -149.0, -792.0, 326.0, 1212.0, -491.0, 104.0, 405.0, -125.0, -454.0, -49.0, -368.0, -122.0, -524.0, -455.0, -344.0, 44.0, -273.0, -93.0, 138.0, 26.0, 534.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0, 1074.0, -455.0, -371.0, 1087.0, 747.0, 1430.0, -86.0, 962.0, 493.0, 570.0, 1273.0, -406.0, 51.0, 751.0, -294.0, 1090.0, 1111.0, 1865.0, 654.0, 1060.0, 1502.0, 1190.0, 1306.0, 180.0, 1603.0, 477.0, 14.0, 576.0, 3000.0, 295.0, 1798.0, 1398.0, 2381.0, 989.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0, 1253.0, -411.0, 782.0, 851.0, -332.0, -187.0, -617.0, -41006.0, -22.0, -44651.0, -359.0, -526.0, -313.0, -716.0, -4139.0, -562.0, -2916.0, -491.0, -397.0, -414.0, 1097.0, -40135.0, -666.0, -52680.0, 284.0, -588.0, -79539.0, -407.0, 846.0, -284.0, -39.0, -742.0, 816.0, -121.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0, 239.0, -443.0, -94.0, -28346.0, -368.0, 1349.0, -503.0, -40200.0, -448.0, -46285.0, -778.0, -421.0, -403.0, -1328.0, -4147.0, -858.0, 112.0, -502.0, 287.0, -347.0, -1084.0, -37773.0, 504.0, -56854.0, 359.0, 107.0, -82842.0, -3742.0, -653.0, -924.0, 1258.0, -297.0, -6061.0, 985.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/medium/medium28.lay', '-c', '--timeout', '120']
Pacman died! Score: 432
Average Score: 432.0
Scores:        432.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/medium/medium28.lay', '-c', '--timeout', '120']
Pacman died! Score: -4
Average Score: -4.0
Scores:        -4.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/medium/medium28.lay', '-c', '--timeout', '120']
Pacman died! Score: -305
Average Score: -305.0
Scores:        -305.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/medium/medium28.lay', '-c', '--timeout', '120']
Pacman died! Score: -51
Average Score: -51.0
Scores:        -51.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60'], ['-l', '/small/small24.lay', '-c', '--timeout', '60'], ['-l', '/small/small25.lay', '-c', '--timeout', '60'], ['-l', '/small/small26.lay', '-c', '--timeout', '60'], ['-l', '/small/small27.lay', '-c', '--timeout', '60'], ['-l', '/small/small28.lay', '-c', '--timeout', '60'], ['-l', '/small/small29.lay', '-c', '--timeout', '60'], ['-l', '/small/small30.lay', '-c', '--timeout', '60'], ['-l', '/medium/medium1.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium2.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium3.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium4.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium5.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium6.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium7.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium8.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium9.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium10.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium11.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium12.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium13.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium14.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium15.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium16.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium17.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium18.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium19.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium20.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium21.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium22.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium23.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium24.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium25.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium26.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium27.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium28.lay', '-c', '--timeout', '120']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0, -6.0, -478.0, -437.0, 21.0, -266.0, -264.0, -515.0, -212.0, 796.0, 81.0, 226.0, -482.0, -491.0, -149.0, -792.0, 326.0, 1212.0, -491.0, 104.0, 405.0, -125.0, -454.0, -49.0, -368.0, -122.0, -524.0, -455.0, -344.0, 44.0, -273.0, -93.0, 138.0, 26.0, 534.0, 432.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0, 1074.0, -455.0, -371.0, 1087.0, 747.0, 1430.0, -86.0, 962.0, 493.0, 570.0, 1273.0, -406.0, 51.0, 751.0, -294.0, 1090.0, 1111.0, 1865.0, 654.0, 1060.0, 1502.0, 1190.0, 1306.0, 180.0, 1603.0, 477.0, 14.0, 576.0, 3000.0, 295.0, 1798.0, 1398.0, 2381.0, 989.0, -4.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0, 1253.0, -411.0, 782.0, 851.0, -332.0, -187.0, -617.0, -41006.0, -22.0, -44651.0, -359.0, -526.0, -313.0, -716.0, -4139.0, -562.0, -2916.0, -491.0, -397.0, -414.0, 1097.0, -40135.0, -666.0, -52680.0, 284.0, -588.0, -79539.0, -407.0, 846.0, -284.0, -39.0, -742.0, 816.0, -121.0, -305.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0, 239.0, -443.0, -94.0, -28346.0, -368.0, 1349.0, -503.0, -40200.0, -448.0, -46285.0, -778.0, -421.0, -403.0, -1328.0, -4147.0, -858.0, 112.0, -502.0, 287.0, -347.0, -1084.0, -37773.0, 504.0, -56854.0, 359.0, 107.0, -82842.0, -3742.0, -653.0, -924.0, 1258.0, -297.0, -6061.0, 985.0, -51.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/medium/medium29.lay', '-c', '--timeout', '120']
Pacman died! Score: -227
Average Score: -227.0
Scores:        -227.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/medium/medium29.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: 1170.0
Scores:        1170.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/medium/medium29.lay', '-c', '--timeout', '120']
Pacman died! Score: -547
Average Score: -547.0
Scores:        -547.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/medium/medium29.lay', '-c', '--timeout', '120']
Pacman died! Score: -343
Average Score: -343.0
Scores:        -343.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60'], ['-l', '/small/small24.lay', '-c', '--timeout', '60'], ['-l', '/small/small25.lay', '-c', '--timeout', '60'], ['-l', '/small/small26.lay', '-c', '--timeout', '60'], ['-l', '/small/small27.lay', '-c', '--timeout', '60'], ['-l', '/small/small28.lay', '-c', '--timeout', '60'], ['-l', '/small/small29.lay', '-c', '--timeout', '60'], ['-l', '/small/small30.lay', '-c', '--timeout', '60'], ['-l', '/medium/medium1.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium2.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium3.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium4.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium5.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium6.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium7.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium8.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium9.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium10.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium11.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium12.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium13.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium14.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium15.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium16.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium17.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium18.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium19.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium20.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium21.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium22.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium23.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium24.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium25.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium26.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium27.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium28.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium29.lay', '-c', '--timeout', '120']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0, -6.0, -478.0, -437.0, 21.0, -266.0, -264.0, -515.0, -212.0, 796.0, 81.0, 226.0, -482.0, -491.0, -149.0, -792.0, 326.0, 1212.0, -491.0, 104.0, 405.0, -125.0, -454.0, -49.0, -368.0, -122.0, -524.0, -455.0, -344.0, 44.0, -273.0, -93.0, 138.0, 26.0, 534.0, 432.0, -227.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0, 1074.0, -455.0, -371.0, 1087.0, 747.0, 1430.0, -86.0, 962.0, 493.0, 570.0, 1273.0, -406.0, 51.0, 751.0, -294.0, 1090.0, 1111.0, 1865.0, 654.0, 1060.0, 1502.0, 1190.0, 1306.0, 180.0, 1603.0, 477.0, 14.0, 576.0, 3000.0, 295.0, 1798.0, 1398.0, 2381.0, 989.0, -4.0, 1170.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0, 1253.0, -411.0, 782.0, 851.0, -332.0, -187.0, -617.0, -41006.0, -22.0, -44651.0, -359.0, -526.0, -313.0, -716.0, -4139.0, -562.0, -2916.0, -491.0, -397.0, -414.0, 1097.0, -40135.0, -666.0, -52680.0, 284.0, -588.0, -79539.0, -407.0, 846.0, -284.0, -39.0, -742.0, 816.0, -121.0, -305.0, -547.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0, 239.0, -443.0, -94.0, -28346.0, -368.0, 1349.0, -503.0, -40200.0, -448.0, -46285.0, -778.0, -421.0, -403.0, -1328.0, -4147.0, -858.0, 112.0, -502.0, 287.0, -347.0, -1084.0, -37773.0, 504.0, -56854.0, 359.0, 107.0, -82842.0, -3742.0, -653.0, -924.0, 1258.0, -297.0, -6061.0, 985.0, -51.0, -343.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/medium/medium30.lay', '-c', '--timeout', '120']
Pacman died! Score: -27
Average Score: -27.0
Scores:        -27.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/medium/medium30.lay', '-c', '--timeout', '120']
Pacman crashed
Average Score: 813.0
Scores:        813.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/medium/medium30.lay', '-c', '--timeout', '120']
Pacman died! Score: -1374
Average Score: -1374.0
Scores:        -1374.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/medium/medium30.lay', '-c', '--timeout', '120']
Pacman died! Score: -857
Average Score: -857.0
Scores:        -857.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', 'minimaxClassic', '-c', '--timeout', '60'], ['-l', 'testClassic', '-c', '--timeout', '60'], ['-l', 'smallClassic', '-c', '--timeout', '60'], ['-l', '/small/small1.lay', '-c', '--timeout', '60'], ['-l', '/small/small2.lay', '-c', '--timeout', '60'], ['-l', '/small/small3.lay', '-c', '--timeout', '60'], ['-l', '/small/small4.lay', '-c', '--timeout', '60'], ['-l', '/small/small5.lay', '-c', '--timeout', '60'], ['-l', '/small/small6.lay', '-c', '--timeout', '60'], ['-l', '/small/small7.lay', '-c', '--timeout', '60'], ['-l', '/small/small8.lay', '-c', '--timeout', '60'], ['-l', '/small/small9.lay', '-c', '--timeout', '60'], ['-l', '/small/small10.lay', '-c', '--timeout', '60'], ['-l', '/small/small11.lay', '-c', '--timeout', '60'], ['-l', '/small/small12.lay', '-c', '--timeout', '60'], ['-l', '/small/small13.lay', '-c', '--timeout', '60'], ['-l', '/small/small14.lay', '-c', '--timeout', '60'], ['-l', '/small/small15.lay', '-c', '--timeout', '60'], ['-l', '/small/small16.lay', '-c', '--timeout', '60'], ['-l', '/small/small17.lay', '-c', '--timeout', '60'], ['-l', '/small/small18.lay', '-c', '--timeout', '60'], ['-l', '/small/small19.lay', '-c', '--timeout', '60'], ['-l', '/small/small20.lay', '-c', '--timeout', '60'], ['-l', '/small/small21.lay', '-c', '--timeout', '60'], ['-l', '/small/small22.lay', '-c', '--timeout', '60'], ['-l', '/small/small23.lay', '-c', '--timeout', '60'], ['-l', '/small/small24.lay', '-c', '--timeout', '60'], ['-l', '/small/small25.lay', '-c', '--timeout', '60'], ['-l', '/small/small26.lay', '-c', '--timeout', '60'], ['-l', '/small/small27.lay', '-c', '--timeout', '60'], ['-l', '/small/small28.lay', '-c', '--timeout', '60'], ['-l', '/small/small29.lay', '-c', '--timeout', '60'], ['-l', '/small/small30.lay', '-c', '--timeout', '60'], ['-l', '/medium/medium1.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium2.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium3.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium4.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium5.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium6.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium7.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium8.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium9.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium10.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium11.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium12.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium13.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium14.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium15.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium16.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium17.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium18.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium19.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium20.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium21.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium22.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium23.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium24.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium25.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium26.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium27.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium28.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium29.lay', '-c', '--timeout', '120'], ['-l', '/medium/medium30.lay', '-c', '--timeout', '120']]
Scores:  [530.0, -147.0, -492.0, -518.0, -375.0, -460.0, 249.0, 750.0, -429.0, -423.0, 81.0, 78.0, -491.0, -462.0, 200.0, -492.0, 321.0, -473.0, -419.0, -224.0, -245.0, -628.0, -482.0, -359.0, -137.0, 101.0, -90.0, -471.0, -6.0, -478.0, -437.0, 21.0, -266.0, -264.0, -515.0, -212.0, 796.0, 81.0, 226.0, -482.0, -491.0, -149.0, -792.0, 326.0, 1212.0, -491.0, 104.0, 405.0, -125.0, -454.0, -49.0, -368.0, -122.0, -524.0, -455.0, -344.0, 44.0, -273.0, -93.0, 138.0, 26.0, 534.0, 432.0, -227.0, -27.0] [542.0, 1501.0, 516.0, 560.0, -339.0, -395.0, -478.0, 828.0, -405.0, -492.0, -440.0, 1472.0, -261.0, -425.0, -487.0, -458.0, 1722.0, -482.0, 293.0, 234.0, -48.0, -377.0, -427.0, 76.0, 1098.0, 477.0, 1275.0, 776.0, 1074.0, -455.0, -371.0, 1087.0, 747.0, 1430.0, -86.0, 962.0, 493.0, 570.0, 1273.0, -406.0, 51.0, 751.0, -294.0, 1090.0, 1111.0, 1865.0, 654.0, 1060.0, 1502.0, 1190.0, 1306.0, 180.0, 1603.0, 477.0, 14.0, 576.0, 3000.0, 295.0, 1798.0, 1398.0, 2381.0, 989.0, -4.0, 1170.0, 813.0] [482.0, -220.0, 516.0, 516.0, -188.0, -464.0, 1619.0, 0.0, 661.0, -492.0, -513.0, 1729.0, -491.0, -457.0, -473.0, -439.0, 415.0, -461.0, -109.0, -25814.0, -459.0, -45017.0, -429.0, -457.0, -604.0, -650.0, -436.0, 581.0, 1253.0, -411.0, 782.0, 851.0, -332.0, -187.0, -617.0, -41006.0, -22.0, -44651.0, -359.0, -526.0, -313.0, -716.0, -4139.0, -562.0, -2916.0, -491.0, -397.0, -414.0, 1097.0, -40135.0, -666.0, -52680.0, 284.0, -588.0, -79539.0, -407.0, 846.0, -284.0, -39.0, -742.0, 816.0, -121.0, -305.0, -547.0, -1374.0] [520.0, -426.0, 516.0, 508.0, -137.0, -583.0, -220.0, 0.0, 651.0, -576.0, -438.0, 1800.0, -1617.0, -499.0, -451.0, -490.0, 778.0, -438.0, 66.0, 1582.0, 766.0, -46483.0, 609.0, -908.0, 332.0, -70.0, -333.0, 773.0, 239.0, -443.0, -94.0, -28346.0, -368.0, 1349.0, -503.0, -40200.0, -448.0, -46285.0, -778.0, -421.0, -403.0, -1328.0, -4147.0, -858.0, 112.0, -502.0, 287.0, -347.0, -1084.0, -37773.0, 504.0, -56854.0, 359.0, 107.0, -82842.0, -3742.0, -653.0, -924.0, 1258.0, -297.0, -6061.0, 985.0, -51.0, -343.0, -857.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/big/big1.lay', '-c', '--timeout', '180']

Traceback (most recent call last):
  File "/Users/sachinbellamkonda/Desktop/cse571_mcts/testMcts.py", line 178, in <module>
    runLargeEnvs(1, 30)
  File "/Users/sachinbellamkonda/Desktop/cse571_mcts/testMcts.py", line 91, in runLargeEnvs
    runScript(layoutName,'large')
  File "/Users/sachinbellamkonda/Desktop/cse571_mcts/testMcts.py", line 109, in runScript
    scores1.append(execute_program(args1))
                   ^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sachinbellamkonda/Desktop/cse571_mcts/testMcts.py", line 40, in execute_program
    score_match = re.search(r"Score: (-?\d+)", output.split('\n')[1])
                                               ~~~~~~~~~~~~~~~~~~^^^
IndexError: list index out of range
(base) sachinbellamkonda@Sachins-MacBook-Air cse571_mcts % python testMcts.py
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/large/large1.lay', '-c', '--timeout', '180']
Pacman died! Score: -444
Average Score: -444.0
Scores:        -444.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/large/large1.lay', '-c', '--timeout', '180']
Pacman died! Score: -13
Average Score: -13.0
Scores:        -13.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/large/large1.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: -36.0
Scores:        -36.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/large/large1.lay', '-c', '--timeout', '180']
Pacman died! Score: -109
Average Score: -109.0
Scores:        -109.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', '/large/large1.lay', '-c', '--timeout', '180']]
Scores:  [-444.0] [-13.0] [-36.0] [-109.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/large/large2.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 712.0
Scores:        712.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/large/large2.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 1046.0
Scores:        1046.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/large/large2.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 180.0
Scores:        180.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/large/large2.lay', '-c', '--timeout', '180']
Pacman died! Score: -394
Average Score: -394.0
Scores:        -394.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', '/large/large1.lay', '-c', '--timeout', '180'], ['-l', '/large/large2.lay', '-c', '--timeout', '180']]
Scores:  [-444.0, 712.0] [-13.0, 1046.0] [-36.0, 180.0] [-109.0, -394.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/large/large3.lay', '-c', '--timeout', '180']
Pacman died! Score: 7
Average Score: 7.0
Scores:        7.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/large/large3.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 289.0
Scores:        289.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/large/large3.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 108.0
Scores:        108.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/large/large3.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 36.0
Scores:        36.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', '/large/large1.lay', '-c', '--timeout', '180'], ['-l', '/large/large2.lay', '-c', '--timeout', '180'], ['-l', '/large/large3.lay', '-c', '--timeout', '180']]
Scores:  [-444.0, 712.0, 7.0] [-13.0, 1046.0, 289.0] [-36.0, 180.0, 108.0] [-109.0, -394.0, 36.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/large/large4.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 768.0
Scores:        768.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/large/large4.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 552.0
Scores:        552.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/large/large4.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: -749.0
Scores:        -749.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/large/large4.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: -775.0
Scores:        -775.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', '/large/large1.lay', '-c', '--timeout', '180'], ['-l', '/large/large2.lay', '-c', '--timeout', '180'], ['-l', '/large/large3.lay', '-c', '--timeout', '180'], ['-l', '/large/large4.lay', '-c', '--timeout', '180']]
Scores:  [-444.0, 712.0, 7.0, 768.0] [-13.0, 1046.0, 289.0, 552.0] [-36.0, 180.0, 108.0, -749.0] [-109.0, -394.0, 36.0, -775.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/large/large5.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 290.0
Scores:        290.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/large/large5.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 547.0
Scores:        547.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/large/large5.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 131.0
Scores:        131.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/large/large5.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 137.0
Scores:        137.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', '/large/large1.lay', '-c', '--timeout', '180'], ['-l', '/large/large2.lay', '-c', '--timeout', '180'], ['-l', '/large/large3.lay', '-c', '--timeout', '180'], ['-l', '/large/large4.lay', '-c', '--timeout', '180'], ['-l', '/large/large5.lay', '-c', '--timeout', '180']]
Scores:  [-444.0, 712.0, 7.0, 768.0, 290.0] [-13.0, 1046.0, 289.0, 552.0, 547.0] [-36.0, 180.0, 108.0, -749.0, 131.0] [-109.0, -394.0, 36.0, -775.0, 137.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/large/large6.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 467.0
Scores:        467.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/large/large6.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 459.0
Scores:        459.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/large/large6.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 378.0
Scores:        378.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/large/large6.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 207.0
Scores:        207.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', '/large/large1.lay', '-c', '--timeout', '180'], ['-l', '/large/large2.lay', '-c', '--timeout', '180'], ['-l', '/large/large3.lay', '-c', '--timeout', '180'], ['-l', '/large/large4.lay', '-c', '--timeout', '180'], ['-l', '/large/large5.lay', '-c', '--timeout', '180'], ['-l', '/large/large6.lay', '-c', '--timeout', '180']]
Scores:  [-444.0, 712.0, 7.0, 768.0, 290.0, 467.0] [-13.0, 1046.0, 289.0, 552.0, 547.0, 459.0] [-36.0, 180.0, 108.0, -749.0, 131.0, 378.0] [-109.0, -394.0, 36.0, -775.0, 137.0, 207.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/large/large7.lay', '-c', '--timeout', '180']
Pacman died! Score: -542
Average Score: -542.0
Scores:        -542.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/large/large7.lay', '-c', '--timeout', '180']
Pacman died! Score: 316
Average Score: 316.0
Scores:        316.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/large/large7.lay', '-c', '--timeout', '180']
Pacman died! Score: -460
Average Score: -460.0
Scores:        -460.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/large/large7.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 1256.0
Scores:        1256.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', '/large/large1.lay', '-c', '--timeout', '180'], ['-l', '/large/large2.lay', '-c', '--timeout', '180'], ['-l', '/large/large3.lay', '-c', '--timeout', '180'], ['-l', '/large/large4.lay', '-c', '--timeout', '180'], ['-l', '/large/large5.lay', '-c', '--timeout', '180'], ['-l', '/large/large6.lay', '-c', '--timeout', '180'], ['-l', '/large/large7.lay', '-c', '--timeout', '180']]
Scores:  [-444.0, 712.0, 7.0, 768.0, 290.0, 467.0, -542.0] [-13.0, 1046.0, 289.0, 552.0, 547.0, 459.0, 316.0] [-36.0, 180.0, 108.0, -749.0, 131.0, 378.0, -460.0] [-109.0, -394.0, 36.0, -775.0, 137.0, 207.0, 1256.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/large/large8.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 926.0
Scores:        926.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/large/large8.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 1525.0
Scores:        1525.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/large/large8.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 405.0
Scores:        405.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/large/large8.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 117.0
Scores:        117.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', '/large/large1.lay', '-c', '--timeout', '180'], ['-l', '/large/large2.lay', '-c', '--timeout', '180'], ['-l', '/large/large3.lay', '-c', '--timeout', '180'], ['-l', '/large/large4.lay', '-c', '--timeout', '180'], ['-l', '/large/large5.lay', '-c', '--timeout', '180'], ['-l', '/large/large6.lay', '-c', '--timeout', '180'], ['-l', '/large/large7.lay', '-c', '--timeout', '180'], ['-l', '/large/large8.lay', '-c', '--timeout', '180']]
Scores:  [-444.0, 712.0, 7.0, 768.0, 290.0, 467.0, -542.0, 926.0] [-13.0, 1046.0, 289.0, 552.0, 547.0, 459.0, 316.0, 1525.0] [-36.0, 180.0, 108.0, -749.0, 131.0, 378.0, -460.0, 405.0] [-109.0, -394.0, 36.0, -775.0, 137.0, 207.0, 1256.0, 117.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/large/large9.lay', '-c', '--timeout', '180']
Pacman died! Score: -17
Average Score: -17.0
Scores:        -17.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/large/large9.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 581.0
Scores:        581.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/large/large9.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 99.0
Scores:        99.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/large/large9.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 63.0
Scores:        63.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', '/large/large1.lay', '-c', '--timeout', '180'], ['-l', '/large/large2.lay', '-c', '--timeout', '180'], ['-l', '/large/large3.lay', '-c', '--timeout', '180'], ['-l', '/large/large4.lay', '-c', '--timeout', '180'], ['-l', '/large/large5.lay', '-c', '--timeout', '180'], ['-l', '/large/large6.lay', '-c', '--timeout', '180'], ['-l', '/large/large7.lay', '-c', '--timeout', '180'], ['-l', '/large/large8.lay', '-c', '--timeout', '180'], ['-l', '/large/large9.lay', '-c', '--timeout', '180']]
Scores:  [-444.0, 712.0, 7.0, 768.0, 290.0, 467.0, -542.0, 926.0, -17.0] [-13.0, 1046.0, 289.0, 552.0, 547.0, 459.0, 316.0, 1525.0, 581.0] [-36.0, 180.0, 108.0, -749.0, 131.0, 378.0, -460.0, 405.0, 99.0] [-109.0, -394.0, 36.0, -775.0, 137.0, 207.0, 1256.0, 117.0, 63.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/large/large10.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 880.0
Scores:        880.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/large/large10.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 2159.0
Scores:        2159.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/large/large10.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 135.0
Scores:        135.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/large/large10.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 27.0
Scores:        27.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', '/large/large1.lay', '-c', '--timeout', '180'], ['-l', '/large/large2.lay', '-c', '--timeout', '180'], ['-l', '/large/large3.lay', '-c', '--timeout', '180'], ['-l', '/large/large4.lay', '-c', '--timeout', '180'], ['-l', '/large/large5.lay', '-c', '--timeout', '180'], ['-l', '/large/large6.lay', '-c', '--timeout', '180'], ['-l', '/large/large7.lay', '-c', '--timeout', '180'], ['-l', '/large/large8.lay', '-c', '--timeout', '180'], ['-l', '/large/large9.lay', '-c', '--timeout', '180'], ['-l', '/large/large10.lay', '-c', '--timeout', '180']]
Scores:  [-444.0, 712.0, 7.0, 768.0, 290.0, 467.0, -542.0, 926.0, -17.0, 880.0] [-13.0, 1046.0, 289.0, 552.0, 547.0, 459.0, 316.0, 1525.0, 581.0, 2159.0] [-36.0, 180.0, 108.0, -749.0, 131.0, 378.0, -460.0, 405.0, 99.0, 135.0] [-109.0, -394.0, 36.0, -775.0, 137.0, 207.0, 1256.0, 117.0, 63.0, 27.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/large/large11.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 497.0
Scores:        497.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/large/large11.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 709.0
Scores:        709.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/large/large11.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 207.0
Scores:        207.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/large/large11.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 9.0
Scores:        9.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', '/large/large1.lay', '-c', '--timeout', '180'], ['-l', '/large/large2.lay', '-c', '--timeout', '180'], ['-l', '/large/large3.lay', '-c', '--timeout', '180'], ['-l', '/large/large4.lay', '-c', '--timeout', '180'], ['-l', '/large/large5.lay', '-c', '--timeout', '180'], ['-l', '/large/large6.lay', '-c', '--timeout', '180'], ['-l', '/large/large7.lay', '-c', '--timeout', '180'], ['-l', '/large/large8.lay', '-c', '--timeout', '180'], ['-l', '/large/large9.lay', '-c', '--timeout', '180'], ['-l', '/large/large10.lay', '-c', '--timeout', '180'], ['-l', '/large/large11.lay', '-c', '--timeout', '180']]
Scores:  [-444.0, 712.0, 7.0, 768.0, 290.0, 467.0, -542.0, 926.0, -17.0, 880.0, 497.0] [-13.0, 1046.0, 289.0, 552.0, 547.0, 459.0, 316.0, 1525.0, 581.0, 2159.0, 709.0] [-36.0, 180.0, 108.0, -749.0, 131.0, 378.0, -460.0, 405.0, 99.0, 135.0, 207.0] [-109.0, -394.0, 36.0, -775.0, 137.0, 207.0, 1256.0, 117.0, 63.0, 27.0, 9.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/large/large12.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 265.0
Scores:        265.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/large/large12.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 829.0
Scores:        829.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/large/large12.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 233.0
Scores:        233.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/large/large12.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 54.0
Scores:        54.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', '/large/large1.lay', '-c', '--timeout', '180'], ['-l', '/large/large2.lay', '-c', '--timeout', '180'], ['-l', '/large/large3.lay', '-c', '--timeout', '180'], ['-l', '/large/large4.lay', '-c', '--timeout', '180'], ['-l', '/large/large5.lay', '-c', '--timeout', '180'], ['-l', '/large/large6.lay', '-c', '--timeout', '180'], ['-l', '/large/large7.lay', '-c', '--timeout', '180'], ['-l', '/large/large8.lay', '-c', '--timeout', '180'], ['-l', '/large/large9.lay', '-c', '--timeout', '180'], ['-l', '/large/large10.lay', '-c', '--timeout', '180'], ['-l', '/large/large11.lay', '-c', '--timeout', '180'], ['-l', '/large/large12.lay', '-c', '--timeout', '180']]
Scores:  [-444.0, 712.0, 7.0, 768.0, 290.0, 467.0, -542.0, 926.0, -17.0, 880.0, 497.0, 265.0] [-13.0, 1046.0, 289.0, 552.0, 547.0, 459.0, 316.0, 1525.0, 581.0, 2159.0, 709.0, 829.0] [-36.0, 180.0, 108.0, -749.0, 131.0, 378.0, -460.0, 405.0, 99.0, 135.0, 207.0, 233.0] [-109.0, -394.0, 36.0, -775.0, 137.0, 207.0, 1256.0, 117.0, 63.0, 27.0, 9.0, 54.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/large/large13.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 643.0
Scores:        643.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/large/large13.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 773.0
Scores:        773.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/large/large13.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 108.0
Scores:        108.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/large/large13.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 63.0
Scores:        63.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', '/large/large1.lay', '-c', '--timeout', '180'], ['-l', '/large/large2.lay', '-c', '--timeout', '180'], ['-l', '/large/large3.lay', '-c', '--timeout', '180'], ['-l', '/large/large4.lay', '-c', '--timeout', '180'], ['-l', '/large/large5.lay', '-c', '--timeout', '180'], ['-l', '/large/large6.lay', '-c', '--timeout', '180'], ['-l', '/large/large7.lay', '-c', '--timeout', '180'], ['-l', '/large/large8.lay', '-c', '--timeout', '180'], ['-l', '/large/large9.lay', '-c', '--timeout', '180'], ['-l', '/large/large10.lay', '-c', '--timeout', '180'], ['-l', '/large/large11.lay', '-c', '--timeout', '180'], ['-l', '/large/large12.lay', '-c', '--timeout', '180'], ['-l', '/large/large13.lay', '-c', '--timeout', '180']]
Scores:  [-444.0, 712.0, 7.0, 768.0, 290.0, 467.0, -542.0, 926.0, -17.0, 880.0, 497.0, 265.0, 643.0] [-13.0, 1046.0, 289.0, 552.0, 547.0, 459.0, 316.0, 1525.0, 581.0, 2159.0, 709.0, 829.0, 773.0] [-36.0, 180.0, 108.0, -749.0, 131.0, 378.0, -460.0, 405.0, 99.0, 135.0, 207.0, 233.0, 108.0] [-109.0, -394.0, 36.0, -775.0, 137.0, 207.0, 1256.0, 117.0, 63.0, 27.0, 9.0, 54.0, 63.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/large/large14.lay', '-c', '--timeout', '180']
Pacman died! Score: 296
Average Score: 296.0
Scores:        296.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/large/large14.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 1291.0
Scores:        1291.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/large/large14.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 904.0
Scores:        904.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/large/large14.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 534.0
Scores:        534.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', '/large/large1.lay', '-c', '--timeout', '180'], ['-l', '/large/large2.lay', '-c', '--timeout', '180'], ['-l', '/large/large3.lay', '-c', '--timeout', '180'], ['-l', '/large/large4.lay', '-c', '--timeout', '180'], ['-l', '/large/large5.lay', '-c', '--timeout', '180'], ['-l', '/large/large6.lay', '-c', '--timeout', '180'], ['-l', '/large/large7.lay', '-c', '--timeout', '180'], ['-l', '/large/large8.lay', '-c', '--timeout', '180'], ['-l', '/large/large9.lay', '-c', '--timeout', '180'], ['-l', '/large/large10.lay', '-c', '--timeout', '180'], ['-l', '/large/large11.lay', '-c', '--timeout', '180'], ['-l', '/large/large12.lay', '-c', '--timeout', '180'], ['-l', '/large/large13.lay', '-c', '--timeout', '180'], ['-l', '/large/large14.lay', '-c', '--timeout', '180']]
Scores:  [-444.0, 712.0, 7.0, 768.0, 290.0, 467.0, -542.0, 926.0, -17.0, 880.0, 497.0, 265.0, 643.0, 296.0] [-13.0, 1046.0, 289.0, 552.0, 547.0, 459.0, 316.0, 1525.0, 581.0, 2159.0, 709.0, 829.0, 773.0, 1291.0] [-36.0, 180.0, 108.0, -749.0, 131.0, 378.0, -460.0, 405.0, 99.0, 135.0, 207.0, 233.0, 108.0, 904.0] [-109.0, -394.0, 36.0, -775.0, 137.0, 207.0, 1256.0, 117.0, 63.0, 27.0, 9.0, 54.0, 63.0, 534.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/large/large15.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 563.0
Scores:        563.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/large/large15.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 1807.0
Scores:        1807.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/large/large15.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 305.0
Scores:        305.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/large/large15.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 153.0
Scores:        153.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', '/large/large1.lay', '-c', '--timeout', '180'], ['-l', '/large/large2.lay', '-c', '--timeout', '180'], ['-l', '/large/large3.lay', '-c', '--timeout', '180'], ['-l', '/large/large4.lay', '-c', '--timeout', '180'], ['-l', '/large/large5.lay', '-c', '--timeout', '180'], ['-l', '/large/large6.lay', '-c', '--timeout', '180'], ['-l', '/large/large7.lay', '-c', '--timeout', '180'], ['-l', '/large/large8.lay', '-c', '--timeout', '180'], ['-l', '/large/large9.lay', '-c', '--timeout', '180'], ['-l', '/large/large10.lay', '-c', '--timeout', '180'], ['-l', '/large/large11.lay', '-c', '--timeout', '180'], ['-l', '/large/large12.lay', '-c', '--timeout', '180'], ['-l', '/large/large13.lay', '-c', '--timeout', '180'], ['-l', '/large/large14.lay', '-c', '--timeout', '180'], ['-l', '/large/large15.lay', '-c', '--timeout', '180']]
Scores:  [-444.0, 712.0, 7.0, 768.0, 290.0, 467.0, -542.0, 926.0, -17.0, 880.0, 497.0, 265.0, 643.0, 296.0, 563.0] [-13.0, 1046.0, 289.0, 552.0, 547.0, 459.0, 316.0, 1525.0, 581.0, 2159.0, 709.0, 829.0, 773.0, 1291.0, 1807.0] [-36.0, 180.0, 108.0, -749.0, 131.0, 378.0, -460.0, 405.0, 99.0, 135.0, 207.0, 233.0, 108.0, 904.0, 305.0] [-109.0, -394.0, 36.0, -775.0, 137.0, 207.0, 1256.0, 117.0, 63.0, 27.0, 9.0, 54.0, 63.0, 534.0, 153.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/large/large16.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 874.0
Scores:        874.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/large/large16.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 978.0
Scores:        978.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/large/large16.lay', '-c', '--timeout', '180']
Pacman died! Score: -1510
Average Score: -1510.0
Scores:        -1510.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/large/large16.lay', '-c', '--timeout', '180']
Pacman died! Score: -736
Average Score: -736.0
Scores:        -736.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', '/large/large1.lay', '-c', '--timeout', '180'], ['-l', '/large/large2.lay', '-c', '--timeout', '180'], ['-l', '/large/large3.lay', '-c', '--timeout', '180'], ['-l', '/large/large4.lay', '-c', '--timeout', '180'], ['-l', '/large/large5.lay', '-c', '--timeout', '180'], ['-l', '/large/large6.lay', '-c', '--timeout', '180'], ['-l', '/large/large7.lay', '-c', '--timeout', '180'], ['-l', '/large/large8.lay', '-c', '--timeout', '180'], ['-l', '/large/large9.lay', '-c', '--timeout', '180'], ['-l', '/large/large10.lay', '-c', '--timeout', '180'], ['-l', '/large/large11.lay', '-c', '--timeout', '180'], ['-l', '/large/large12.lay', '-c', '--timeout', '180'], ['-l', '/large/large13.lay', '-c', '--timeout', '180'], ['-l', '/large/large14.lay', '-c', '--timeout', '180'], ['-l', '/large/large15.lay', '-c', '--timeout', '180'], ['-l', '/large/large16.lay', '-c', '--timeout', '180']]
Scores:  [-444.0, 712.0, 7.0, 768.0, 290.0, 467.0, -542.0, 926.0, -17.0, 880.0, 497.0, 265.0, 643.0, 296.0, 563.0, 874.0] [-13.0, 1046.0, 289.0, 552.0, 547.0, 459.0, 316.0, 1525.0, 581.0, 2159.0, 709.0, 829.0, 773.0, 1291.0, 1807.0, 978.0] [-36.0, 180.0, 108.0, -749.0, 131.0, 378.0, -460.0, 405.0, 99.0, 135.0, 207.0, 233.0, 108.0, 904.0, 305.0, -1510.0] [-109.0, -394.0, 36.0, -775.0, 137.0, 207.0, 1256.0, 117.0, 63.0, 27.0, 9.0, 54.0, 63.0, 534.0, 153.0, -736.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/large/large17.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 439.0
Scores:        439.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/large/large17.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 1041.0
Scores:        1041.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/large/large17.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 79.0
Scores:        79.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/large/large17.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 594.0
Scores:        594.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', '/large/large1.lay', '-c', '--timeout', '180'], ['-l', '/large/large2.lay', '-c', '--timeout', '180'], ['-l', '/large/large3.lay', '-c', '--timeout', '180'], ['-l', '/large/large4.lay', '-c', '--timeout', '180'], ['-l', '/large/large5.lay', '-c', '--timeout', '180'], ['-l', '/large/large6.lay', '-c', '--timeout', '180'], ['-l', '/large/large7.lay', '-c', '--timeout', '180'], ['-l', '/large/large8.lay', '-c', '--timeout', '180'], ['-l', '/large/large9.lay', '-c', '--timeout', '180'], ['-l', '/large/large10.lay', '-c', '--timeout', '180'], ['-l', '/large/large11.lay', '-c', '--timeout', '180'], ['-l', '/large/large12.lay', '-c', '--timeout', '180'], ['-l', '/large/large13.lay', '-c', '--timeout', '180'], ['-l', '/large/large14.lay', '-c', '--timeout', '180'], ['-l', '/large/large15.lay', '-c', '--timeout', '180'], ['-l', '/large/large16.lay', '-c', '--timeout', '180'], ['-l', '/large/large17.lay', '-c', '--timeout', '180']]
Scores:  [-444.0, 712.0, 7.0, 768.0, 290.0, 467.0, -542.0, 926.0, -17.0, 880.0, 497.0, 265.0, 643.0, 296.0, 563.0, 874.0, 439.0] [-13.0, 1046.0, 289.0, 552.0, 547.0, 459.0, 316.0, 1525.0, 581.0, 2159.0, 709.0, 829.0, 773.0, 1291.0, 1807.0, 978.0, 1041.0] [-36.0, 180.0, 108.0, -749.0, 131.0, 378.0, -460.0, 405.0, 99.0, 135.0, 207.0, 233.0, 108.0, 904.0, 305.0, -1510.0, 79.0] [-109.0, -394.0, 36.0, -775.0, 137.0, 207.0, 1256.0, 117.0, 63.0, 27.0, 9.0, 54.0, 63.0, 534.0, 153.0, -736.0, 594.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/large/large18.lay', '-c', '--timeout', '180']
Pacman died! Score: 313
Average Score: 313.0
Scores:        313.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/large/large18.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 2277.0
Scores:        2277.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/large/large18.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 81.0
Scores:        81.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/large/large18.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 36.0
Scores:        36.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', '/large/large1.lay', '-c', '--timeout', '180'], ['-l', '/large/large2.lay', '-c', '--timeout', '180'], ['-l', '/large/large3.lay', '-c', '--timeout', '180'], ['-l', '/large/large4.lay', '-c', '--timeout', '180'], ['-l', '/large/large5.lay', '-c', '--timeout', '180'], ['-l', '/large/large6.lay', '-c', '--timeout', '180'], ['-l', '/large/large7.lay', '-c', '--timeout', '180'], ['-l', '/large/large8.lay', '-c', '--timeout', '180'], ['-l', '/large/large9.lay', '-c', '--timeout', '180'], ['-l', '/large/large10.lay', '-c', '--timeout', '180'], ['-l', '/large/large11.lay', '-c', '--timeout', '180'], ['-l', '/large/large12.lay', '-c', '--timeout', '180'], ['-l', '/large/large13.lay', '-c', '--timeout', '180'], ['-l', '/large/large14.lay', '-c', '--timeout', '180'], ['-l', '/large/large15.lay', '-c', '--timeout', '180'], ['-l', '/large/large16.lay', '-c', '--timeout', '180'], ['-l', '/large/large17.lay', '-c', '--timeout', '180'], ['-l', '/large/large18.lay', '-c', '--timeout', '180']]
Scores:  [-444.0, 712.0, 7.0, 768.0, 290.0, 467.0, -542.0, 926.0, -17.0, 880.0, 497.0, 265.0, 643.0, 296.0, 563.0, 874.0, 439.0, 313.0] [-13.0, 1046.0, 289.0, 552.0, 547.0, 459.0, 316.0, 1525.0, 581.0, 2159.0, 709.0, 829.0, 773.0, 1291.0, 1807.0, 978.0, 1041.0, 2277.0] [-36.0, 180.0, 108.0, -749.0, 131.0, 378.0, -460.0, 405.0, 99.0, 135.0, 207.0, 233.0, 108.0, 904.0, 305.0, -1510.0, 79.0, 81.0] [-109.0, -394.0, 36.0, -775.0, 137.0, 207.0, 1256.0, 117.0, 63.0, 27.0, 9.0, 54.0, 63.0, 534.0, 153.0, -736.0, 594.0, 36.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/large/large19.lay', '-c', '--timeout', '180']
Pacman died! Score: -184
Average Score: -184.0
Scores:        -184.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/large/large19.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 1793.0
Scores:        1793.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/large/large19.lay', '-c', '--timeout', '180']
Pacman died! Score: -487
Average Score: -487.0
Scores:        -487.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/large/large19.lay', '-c', '--timeout', '180']
Pacman died! Score: -531
Average Score: -531.0
Scores:        -531.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', '/large/large1.lay', '-c', '--timeout', '180'], ['-l', '/large/large2.lay', '-c', '--timeout', '180'], ['-l', '/large/large3.lay', '-c', '--timeout', '180'], ['-l', '/large/large4.lay', '-c', '--timeout', '180'], ['-l', '/large/large5.lay', '-c', '--timeout', '180'], ['-l', '/large/large6.lay', '-c', '--timeout', '180'], ['-l', '/large/large7.lay', '-c', '--timeout', '180'], ['-l', '/large/large8.lay', '-c', '--timeout', '180'], ['-l', '/large/large9.lay', '-c', '--timeout', '180'], ['-l', '/large/large10.lay', '-c', '--timeout', '180'], ['-l', '/large/large11.lay', '-c', '--timeout', '180'], ['-l', '/large/large12.lay', '-c', '--timeout', '180'], ['-l', '/large/large13.lay', '-c', '--timeout', '180'], ['-l', '/large/large14.lay', '-c', '--timeout', '180'], ['-l', '/large/large15.lay', '-c', '--timeout', '180'], ['-l', '/large/large16.lay', '-c', '--timeout', '180'], ['-l', '/large/large17.lay', '-c', '--timeout', '180'], ['-l', '/large/large18.lay', '-c', '--timeout', '180'], ['-l', '/large/large19.lay', '-c', '--timeout', '180']]
Scores:  [-444.0, 712.0, 7.0, 768.0, 290.0, 467.0, -542.0, 926.0, -17.0, 880.0, 497.0, 265.0, 643.0, 296.0, 563.0, 874.0, 439.0, 313.0, -184.0] [-13.0, 1046.0, 289.0, 552.0, 547.0, 459.0, 316.0, 1525.0, 581.0, 2159.0, 709.0, 829.0, 773.0, 1291.0, 1807.0, 978.0, 1041.0, 2277.0, 1793.0] [-36.0, 180.0, 108.0, -749.0, 131.0, 378.0, -460.0, 405.0, 99.0, 135.0, 207.0, 233.0, 108.0, 904.0, 305.0, -1510.0, 79.0, 81.0, -487.0] [-109.0, -394.0, 36.0, -775.0, 137.0, 207.0, 1256.0, 117.0, 63.0, 27.0, 9.0, 54.0, 63.0, 534.0, 153.0, -736.0, 594.0, 36.0, -531.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/large/large20.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 718.0
Scores:        718.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/large/large20.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 867.0
Scores:        867.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/large/large20.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 271.0
Scores:        271.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/large/large20.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 291.0
Scores:        291.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', '/large/large1.lay', '-c', '--timeout', '180'], ['-l', '/large/large2.lay', '-c', '--timeout', '180'], ['-l', '/large/large3.lay', '-c', '--timeout', '180'], ['-l', '/large/large4.lay', '-c', '--timeout', '180'], ['-l', '/large/large5.lay', '-c', '--timeout', '180'], ['-l', '/large/large6.lay', '-c', '--timeout', '180'], ['-l', '/large/large7.lay', '-c', '--timeout', '180'], ['-l', '/large/large8.lay', '-c', '--timeout', '180'], ['-l', '/large/large9.lay', '-c', '--timeout', '180'], ['-l', '/large/large10.lay', '-c', '--timeout', '180'], ['-l', '/large/large11.lay', '-c', '--timeout', '180'], ['-l', '/large/large12.lay', '-c', '--timeout', '180'], ['-l', '/large/large13.lay', '-c', '--timeout', '180'], ['-l', '/large/large14.lay', '-c', '--timeout', '180'], ['-l', '/large/large15.lay', '-c', '--timeout', '180'], ['-l', '/large/large16.lay', '-c', '--timeout', '180'], ['-l', '/large/large17.lay', '-c', '--timeout', '180'], ['-l', '/large/large18.lay', '-c', '--timeout', '180'], ['-l', '/large/large19.lay', '-c', '--timeout', '180'], ['-l', '/large/large20.lay', '-c', '--timeout', '180']]
Scores:  [-444.0, 712.0, 7.0, 768.0, 290.0, 467.0, -542.0, 926.0, -17.0, 880.0, 497.0, 265.0, 643.0, 296.0, 563.0, 874.0, 439.0, 313.0, -184.0, 718.0] [-13.0, 1046.0, 289.0, 552.0, 547.0, 459.0, 316.0, 1525.0, 581.0, 2159.0, 709.0, 829.0, 773.0, 1291.0, 1807.0, 978.0, 1041.0, 2277.0, 1793.0, 867.0] [-36.0, 180.0, 108.0, -749.0, 131.0, 378.0, -460.0, 405.0, 99.0, 135.0, 207.0, 233.0, 108.0, 904.0, 305.0, -1510.0, 79.0, 81.0, -487.0, 271.0] [-109.0, -394.0, 36.0, -775.0, 137.0, 207.0, 1256.0, 117.0, 63.0, 27.0, 9.0, 54.0, 63.0, 534.0, 153.0, -736.0, 594.0, 36.0, -531.0, 291.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/large/large21.lay', '-c', '--timeout', '180']
Pacman died! Score: -71
Average Score: -71.0
Scores:        -71.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/large/large21.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 1973.0
Scores:        1973.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/large/large21.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 72.0
Scores:        72.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/large/large21.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 18.0
Scores:        18.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', '/large/large1.lay', '-c', '--timeout', '180'], ['-l', '/large/large2.lay', '-c', '--timeout', '180'], ['-l', '/large/large3.lay', '-c', '--timeout', '180'], ['-l', '/large/large4.lay', '-c', '--timeout', '180'], ['-l', '/large/large5.lay', '-c', '--timeout', '180'], ['-l', '/large/large6.lay', '-c', '--timeout', '180'], ['-l', '/large/large7.lay', '-c', '--timeout', '180'], ['-l', '/large/large8.lay', '-c', '--timeout', '180'], ['-l', '/large/large9.lay', '-c', '--timeout', '180'], ['-l', '/large/large10.lay', '-c', '--timeout', '180'], ['-l', '/large/large11.lay', '-c', '--timeout', '180'], ['-l', '/large/large12.lay', '-c', '--timeout', '180'], ['-l', '/large/large13.lay', '-c', '--timeout', '180'], ['-l', '/large/large14.lay', '-c', '--timeout', '180'], ['-l', '/large/large15.lay', '-c', '--timeout', '180'], ['-l', '/large/large16.lay', '-c', '--timeout', '180'], ['-l', '/large/large17.lay', '-c', '--timeout', '180'], ['-l', '/large/large18.lay', '-c', '--timeout', '180'], ['-l', '/large/large19.lay', '-c', '--timeout', '180'], ['-l', '/large/large20.lay', '-c', '--timeout', '180'], ['-l', '/large/large21.lay', '-c', '--timeout', '180']]
Scores:  [-444.0, 712.0, 7.0, 768.0, 290.0, 467.0, -542.0, 926.0, -17.0, 880.0, 497.0, 265.0, 643.0, 296.0, 563.0, 874.0, 439.0, 313.0, -184.0, 718.0, -71.0] [-13.0, 1046.0, 289.0, 552.0, 547.0, 459.0, 316.0, 1525.0, 581.0, 2159.0, 709.0, 829.0, 773.0, 1291.0, 1807.0, 978.0, 1041.0, 2277.0, 1793.0, 867.0, 1973.0] [-36.0, 180.0, 108.0, -749.0, 131.0, 378.0, -460.0, 405.0, 99.0, 135.0, 207.0, 233.0, 108.0, 904.0, 305.0, -1510.0, 79.0, 81.0, -487.0, 271.0, 72.0] [-109.0, -394.0, 36.0, -775.0, 137.0, 207.0, 1256.0, 117.0, 63.0, 27.0, 9.0, 54.0, 63.0, 534.0, 153.0, -736.0, 594.0, 36.0, -531.0, 291.0, 18.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/large/large22.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 1034.0
Scores:        1034.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/large/large22.lay', '-c', '--timeout', '180']
Pacman died! Score: 41
Average Score: 41.0
Scores:        41.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/large/large22.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 126.0
Scores:        126.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/large/large22.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 117.0
Scores:        117.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', '/large/large1.lay', '-c', '--timeout', '180'], ['-l', '/large/large2.lay', '-c', '--timeout', '180'], ['-l', '/large/large3.lay', '-c', '--timeout', '180'], ['-l', '/large/large4.lay', '-c', '--timeout', '180'], ['-l', '/large/large5.lay', '-c', '--timeout', '180'], ['-l', '/large/large6.lay', '-c', '--timeout', '180'], ['-l', '/large/large7.lay', '-c', '--timeout', '180'], ['-l', '/large/large8.lay', '-c', '--timeout', '180'], ['-l', '/large/large9.lay', '-c', '--timeout', '180'], ['-l', '/large/large10.lay', '-c', '--timeout', '180'], ['-l', '/large/large11.lay', '-c', '--timeout', '180'], ['-l', '/large/large12.lay', '-c', '--timeout', '180'], ['-l', '/large/large13.lay', '-c', '--timeout', '180'], ['-l', '/large/large14.lay', '-c', '--timeout', '180'], ['-l', '/large/large15.lay', '-c', '--timeout', '180'], ['-l', '/large/large16.lay', '-c', '--timeout', '180'], ['-l', '/large/large17.lay', '-c', '--timeout', '180'], ['-l', '/large/large18.lay', '-c', '--timeout', '180'], ['-l', '/large/large19.lay', '-c', '--timeout', '180'], ['-l', '/large/large20.lay', '-c', '--timeout', '180'], ['-l', '/large/large21.lay', '-c', '--timeout', '180'], ['-l', '/large/large22.lay', '-c', '--timeout', '180']]
Scores:  [-444.0, 712.0, 7.0, 768.0, 290.0, 467.0, -542.0, 926.0, -17.0, 880.0, 497.0, 265.0, 643.0, 296.0, 563.0, 874.0, 439.0, 313.0, -184.0, 718.0, -71.0, 1034.0] [-13.0, 1046.0, 289.0, 552.0, 547.0, 459.0, 316.0, 1525.0, 581.0, 2159.0, 709.0, 829.0, 773.0, 1291.0, 1807.0, 978.0, 1041.0, 2277.0, 1793.0, 867.0, 1973.0, 41.0] [-36.0, 180.0, 108.0, -749.0, 131.0, 378.0, -460.0, 405.0, 99.0, 135.0, 207.0, 233.0, 108.0, 904.0, 305.0, -1510.0, 79.0, 81.0, -487.0, 271.0, 72.0, 126.0] [-109.0, -394.0, 36.0, -775.0, 137.0, 207.0, 1256.0, 117.0, 63.0, 27.0, 9.0, 54.0, 63.0, 534.0, 153.0, -736.0, 594.0, 36.0, -531.0, 291.0, 18.0, 117.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/large/large23.lay', '-c', '--timeout', '180']
Pacman died! Score: -305
Average Score: -305.0
Scores:        -305.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/large/large23.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 707.0
Scores:        707.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/large/large23.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 308.0
Scores:        308.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/large/large23.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 138.0
Scores:        138.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', '/large/large1.lay', '-c', '--timeout', '180'], ['-l', '/large/large2.lay', '-c', '--timeout', '180'], ['-l', '/large/large3.lay', '-c', '--timeout', '180'], ['-l', '/large/large4.lay', '-c', '--timeout', '180'], ['-l', '/large/large5.lay', '-c', '--timeout', '180'], ['-l', '/large/large6.lay', '-c', '--timeout', '180'], ['-l', '/large/large7.lay', '-c', '--timeout', '180'], ['-l', '/large/large8.lay', '-c', '--timeout', '180'], ['-l', '/large/large9.lay', '-c', '--timeout', '180'], ['-l', '/large/large10.lay', '-c', '--timeout', '180'], ['-l', '/large/large11.lay', '-c', '--timeout', '180'], ['-l', '/large/large12.lay', '-c', '--timeout', '180'], ['-l', '/large/large13.lay', '-c', '--timeout', '180'], ['-l', '/large/large14.lay', '-c', '--timeout', '180'], ['-l', '/large/large15.lay', '-c', '--timeout', '180'], ['-l', '/large/large16.lay', '-c', '--timeout', '180'], ['-l', '/large/large17.lay', '-c', '--timeout', '180'], ['-l', '/large/large18.lay', '-c', '--timeout', '180'], ['-l', '/large/large19.lay', '-c', '--timeout', '180'], ['-l', '/large/large20.lay', '-c', '--timeout', '180'], ['-l', '/large/large21.lay', '-c', '--timeout', '180'], ['-l', '/large/large22.lay', '-c', '--timeout', '180'], ['-l', '/large/large23.lay', '-c', '--timeout', '180']]
Scores:  [-444.0, 712.0, 7.0, 768.0, 290.0, 467.0, -542.0, 926.0, -17.0, 880.0, 497.0, 265.0, 643.0, 296.0, 563.0, 874.0, 439.0, 313.0, -184.0, 718.0, -71.0, 1034.0, -305.0] [-13.0, 1046.0, 289.0, 552.0, 547.0, 459.0, 316.0, 1525.0, 581.0, 2159.0, 709.0, 829.0, 773.0, 1291.0, 1807.0, 978.0, 1041.0, 2277.0, 1793.0, 867.0, 1973.0, 41.0, 707.0] [-36.0, 180.0, 108.0, -749.0, 131.0, 378.0, -460.0, 405.0, 99.0, 135.0, 207.0, 233.0, 108.0, 904.0, 305.0, -1510.0, 79.0, 81.0, -487.0, 271.0, 72.0, 126.0, 308.0] [-109.0, -394.0, 36.0, -775.0, 137.0, 207.0, 1256.0, 117.0, 63.0, 27.0, 9.0, 54.0, 63.0, 534.0, 153.0, -736.0, 594.0, 36.0, -531.0, 291.0, 18.0, 117.0, 138.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/large/large24.lay', '-c', '--timeout', '180']
Pacman died! Score: -82
Average Score: -82.0
Scores:        -82.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/large/large24.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 1320.0
Scores:        1320.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/large/large24.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 295.0
Scores:        295.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/large/large24.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: -20.0
Scores:        -20.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', '/large/large1.lay', '-c', '--timeout', '180'], ['-l', '/large/large2.lay', '-c', '--timeout', '180'], ['-l', '/large/large3.lay', '-c', '--timeout', '180'], ['-l', '/large/large4.lay', '-c', '--timeout', '180'], ['-l', '/large/large5.lay', '-c', '--timeout', '180'], ['-l', '/large/large6.lay', '-c', '--timeout', '180'], ['-l', '/large/large7.lay', '-c', '--timeout', '180'], ['-l', '/large/large8.lay', '-c', '--timeout', '180'], ['-l', '/large/large9.lay', '-c', '--timeout', '180'], ['-l', '/large/large10.lay', '-c', '--timeout', '180'], ['-l', '/large/large11.lay', '-c', '--timeout', '180'], ['-l', '/large/large12.lay', '-c', '--timeout', '180'], ['-l', '/large/large13.lay', '-c', '--timeout', '180'], ['-l', '/large/large14.lay', '-c', '--timeout', '180'], ['-l', '/large/large15.lay', '-c', '--timeout', '180'], ['-l', '/large/large16.lay', '-c', '--timeout', '180'], ['-l', '/large/large17.lay', '-c', '--timeout', '180'], ['-l', '/large/large18.lay', '-c', '--timeout', '180'], ['-l', '/large/large19.lay', '-c', '--timeout', '180'], ['-l', '/large/large20.lay', '-c', '--timeout', '180'], ['-l', '/large/large21.lay', '-c', '--timeout', '180'], ['-l', '/large/large22.lay', '-c', '--timeout', '180'], ['-l', '/large/large23.lay', '-c', '--timeout', '180'], ['-l', '/large/large24.lay', '-c', '--timeout', '180']]
Scores:  [-444.0, 712.0, 7.0, 768.0, 290.0, 467.0, -542.0, 926.0, -17.0, 880.0, 497.0, 265.0, 643.0, 296.0, 563.0, 874.0, 439.0, 313.0, -184.0, 718.0, -71.0, 1034.0, -305.0, -82.0] [-13.0, 1046.0, 289.0, 552.0, 547.0, 459.0, 316.0, 1525.0, 581.0, 2159.0, 709.0, 829.0, 773.0, 1291.0, 1807.0, 978.0, 1041.0, 2277.0, 1793.0, 867.0, 1973.0, 41.0, 707.0, 1320.0] [-36.0, 180.0, 108.0, -749.0, 131.0, 378.0, -460.0, 405.0, 99.0, 135.0, 207.0, 233.0, 108.0, 904.0, 305.0, -1510.0, 79.0, 81.0, -487.0, 271.0, 72.0, 126.0, 308.0, 295.0] [-109.0, -394.0, 36.0, -775.0, 137.0, 207.0, 1256.0, 117.0, 63.0, 27.0, 9.0, 54.0, 63.0, 534.0, 153.0, -736.0, 594.0, 36.0, -531.0, 291.0, 18.0, 117.0, 138.0, -20.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/large/large25.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 898.0
Scores:        898.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/large/large25.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 1573.0
Scores:        1573.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/large/large25.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 125.0
Scores:        125.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/large/large25.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 131.0
Scores:        131.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', '/large/large1.lay', '-c', '--timeout', '180'], ['-l', '/large/large2.lay', '-c', '--timeout', '180'], ['-l', '/large/large3.lay', '-c', '--timeout', '180'], ['-l', '/large/large4.lay', '-c', '--timeout', '180'], ['-l', '/large/large5.lay', '-c', '--timeout', '180'], ['-l', '/large/large6.lay', '-c', '--timeout', '180'], ['-l', '/large/large7.lay', '-c', '--timeout', '180'], ['-l', '/large/large8.lay', '-c', '--timeout', '180'], ['-l', '/large/large9.lay', '-c', '--timeout', '180'], ['-l', '/large/large10.lay', '-c', '--timeout', '180'], ['-l', '/large/large11.lay', '-c', '--timeout', '180'], ['-l', '/large/large12.lay', '-c', '--timeout', '180'], ['-l', '/large/large13.lay', '-c', '--timeout', '180'], ['-l', '/large/large14.lay', '-c', '--timeout', '180'], ['-l', '/large/large15.lay', '-c', '--timeout', '180'], ['-l', '/large/large16.lay', '-c', '--timeout', '180'], ['-l', '/large/large17.lay', '-c', '--timeout', '180'], ['-l', '/large/large18.lay', '-c', '--timeout', '180'], ['-l', '/large/large19.lay', '-c', '--timeout', '180'], ['-l', '/large/large20.lay', '-c', '--timeout', '180'], ['-l', '/large/large21.lay', '-c', '--timeout', '180'], ['-l', '/large/large22.lay', '-c', '--timeout', '180'], ['-l', '/large/large23.lay', '-c', '--timeout', '180'], ['-l', '/large/large24.lay', '-c', '--timeout', '180'], ['-l', '/large/large25.lay', '-c', '--timeout', '180']]
Scores:  [-444.0, 712.0, 7.0, 768.0, 290.0, 467.0, -542.0, 926.0, -17.0, 880.0, 497.0, 265.0, 643.0, 296.0, 563.0, 874.0, 439.0, 313.0, -184.0, 718.0, -71.0, 1034.0, -305.0, -82.0, 898.0] [-13.0, 1046.0, 289.0, 552.0, 547.0, 459.0, 316.0, 1525.0, 581.0, 2159.0, 709.0, 829.0, 773.0, 1291.0, 1807.0, 978.0, 1041.0, 2277.0, 1793.0, 867.0, 1973.0, 41.0, 707.0, 1320.0, 1573.0] [-36.0, 180.0, 108.0, -749.0, 131.0, 378.0, -460.0, 405.0, 99.0, 135.0, 207.0, 233.0, 108.0, 904.0, 305.0, -1510.0, 79.0, 81.0, -487.0, 271.0, 72.0, 126.0, 308.0, 295.0, 125.0] [-109.0, -394.0, 36.0, -775.0, 137.0, 207.0, 1256.0, 117.0, 63.0, 27.0, 9.0, 54.0, 63.0, 534.0, 153.0, -736.0, 594.0, 36.0, -531.0, 291.0, 18.0, 117.0, 138.0, -20.0, 131.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/large/large26.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 882.0
Scores:        882.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/large/large26.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 870.0
Scores:        870.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/large/large26.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 162.0
Scores:        162.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/large/large26.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 9.0
Scores:        9.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', '/large/large1.lay', '-c', '--timeout', '180'], ['-l', '/large/large2.lay', '-c', '--timeout', '180'], ['-l', '/large/large3.lay', '-c', '--timeout', '180'], ['-l', '/large/large4.lay', '-c', '--timeout', '180'], ['-l', '/large/large5.lay', '-c', '--timeout', '180'], ['-l', '/large/large6.lay', '-c', '--timeout', '180'], ['-l', '/large/large7.lay', '-c', '--timeout', '180'], ['-l', '/large/large8.lay', '-c', '--timeout', '180'], ['-l', '/large/large9.lay', '-c', '--timeout', '180'], ['-l', '/large/large10.lay', '-c', '--timeout', '180'], ['-l', '/large/large11.lay', '-c', '--timeout', '180'], ['-l', '/large/large12.lay', '-c', '--timeout', '180'], ['-l', '/large/large13.lay', '-c', '--timeout', '180'], ['-l', '/large/large14.lay', '-c', '--timeout', '180'], ['-l', '/large/large15.lay', '-c', '--timeout', '180'], ['-l', '/large/large16.lay', '-c', '--timeout', '180'], ['-l', '/large/large17.lay', '-c', '--timeout', '180'], ['-l', '/large/large18.lay', '-c', '--timeout', '180'], ['-l', '/large/large19.lay', '-c', '--timeout', '180'], ['-l', '/large/large20.lay', '-c', '--timeout', '180'], ['-l', '/large/large21.lay', '-c', '--timeout', '180'], ['-l', '/large/large22.lay', '-c', '--timeout', '180'], ['-l', '/large/large23.lay', '-c', '--timeout', '180'], ['-l', '/large/large24.lay', '-c', '--timeout', '180'], ['-l', '/large/large25.lay', '-c', '--timeout', '180'], ['-l', '/large/large26.lay', '-c', '--timeout', '180']]
Scores:  [-444.0, 712.0, 7.0, 768.0, 290.0, 467.0, -542.0, 926.0, -17.0, 880.0, 497.0, 265.0, 643.0, 296.0, 563.0, 874.0, 439.0, 313.0, -184.0, 718.0, -71.0, 1034.0, -305.0, -82.0, 898.0, 882.0] [-13.0, 1046.0, 289.0, 552.0, 547.0, 459.0, 316.0, 1525.0, 581.0, 2159.0, 709.0, 829.0, 773.0, 1291.0, 1807.0, 978.0, 1041.0, 2277.0, 1793.0, 867.0, 1973.0, 41.0, 707.0, 1320.0, 1573.0, 870.0] [-36.0, 180.0, 108.0, -749.0, 131.0, 378.0, -460.0, 405.0, 99.0, 135.0, 207.0, 233.0, 108.0, 904.0, 305.0, -1510.0, 79.0, 81.0, -487.0, 271.0, 72.0, 126.0, 308.0, 295.0, 125.0, 162.0] [-109.0, -394.0, 36.0, -775.0, 137.0, 207.0, 1256.0, 117.0, 63.0, 27.0, 9.0, 54.0, 63.0, 534.0, 153.0, -736.0, 594.0, 36.0, -531.0, 291.0, 18.0, 117.0, 138.0, -20.0, 131.0, 9.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/large/large27.lay', '-c', '--timeout', '180']
Pacman died! Score: -386
Average Score: -386.0
Scores:        -386.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/large/large27.lay', '-c', '--timeout', '180']
Pacman died! Score: 379
Average Score: 379.0
Scores:        379.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/large/large27.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 579.0
Scores:        579.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/large/large27.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 650.0
Scores:        650.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', '/large/large1.lay', '-c', '--timeout', '180'], ['-l', '/large/large2.lay', '-c', '--timeout', '180'], ['-l', '/large/large3.lay', '-c', '--timeout', '180'], ['-l', '/large/large4.lay', '-c', '--timeout', '180'], ['-l', '/large/large5.lay', '-c', '--timeout', '180'], ['-l', '/large/large6.lay', '-c', '--timeout', '180'], ['-l', '/large/large7.lay', '-c', '--timeout', '180'], ['-l', '/large/large8.lay', '-c', '--timeout', '180'], ['-l', '/large/large9.lay', '-c', '--timeout', '180'], ['-l', '/large/large10.lay', '-c', '--timeout', '180'], ['-l', '/large/large11.lay', '-c', '--timeout', '180'], ['-l', '/large/large12.lay', '-c', '--timeout', '180'], ['-l', '/large/large13.lay', '-c', '--timeout', '180'], ['-l', '/large/large14.lay', '-c', '--timeout', '180'], ['-l', '/large/large15.lay', '-c', '--timeout', '180'], ['-l', '/large/large16.lay', '-c', '--timeout', '180'], ['-l', '/large/large17.lay', '-c', '--timeout', '180'], ['-l', '/large/large18.lay', '-c', '--timeout', '180'], ['-l', '/large/large19.lay', '-c', '--timeout', '180'], ['-l', '/large/large20.lay', '-c', '--timeout', '180'], ['-l', '/large/large21.lay', '-c', '--timeout', '180'], ['-l', '/large/large22.lay', '-c', '--timeout', '180'], ['-l', '/large/large23.lay', '-c', '--timeout', '180'], ['-l', '/large/large24.lay', '-c', '--timeout', '180'], ['-l', '/large/large25.lay', '-c', '--timeout', '180'], ['-l', '/large/large26.lay', '-c', '--timeout', '180'], ['-l', '/large/large27.lay', '-c', '--timeout', '180']]
Scores:  [-444.0, 712.0, 7.0, 768.0, 290.0, 467.0, -542.0, 926.0, -17.0, 880.0, 497.0, 265.0, 643.0, 296.0, 563.0, 874.0, 439.0, 313.0, -184.0, 718.0, -71.0, 1034.0, -305.0, -82.0, 898.0, 882.0, -386.0] [-13.0, 1046.0, 289.0, 552.0, 547.0, 459.0, 316.0, 1525.0, 581.0, 2159.0, 709.0, 829.0, 773.0, 1291.0, 1807.0, 978.0, 1041.0, 2277.0, 1793.0, 867.0, 1973.0, 41.0, 707.0, 1320.0, 1573.0, 870.0, 379.0] [-36.0, 180.0, 108.0, -749.0, 131.0, 378.0, -460.0, 405.0, 99.0, 135.0, 207.0, 233.0, 108.0, 904.0, 305.0, -1510.0, 79.0, 81.0, -487.0, 271.0, 72.0, 126.0, 308.0, 295.0, 125.0, 162.0, 579.0] [-109.0, -394.0, 36.0, -775.0, 137.0, 207.0, 1256.0, 117.0, 63.0, 27.0, 9.0, 54.0, 63.0, 534.0, 153.0, -736.0, 594.0, 36.0, -531.0, 291.0, 18.0, 117.0, 138.0, -20.0, 131.0, 9.0, 650.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/large/large28.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 487.0
Scores:        487.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/large/large28.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 1119.0
Scores:        1119.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/large/large28.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 36.0
Scores:        36.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/large/large28.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 9.0
Scores:        9.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', '/large/large1.lay', '-c', '--timeout', '180'], ['-l', '/large/large2.lay', '-c', '--timeout', '180'], ['-l', '/large/large3.lay', '-c', '--timeout', '180'], ['-l', '/large/large4.lay', '-c', '--timeout', '180'], ['-l', '/large/large5.lay', '-c', '--timeout', '180'], ['-l', '/large/large6.lay', '-c', '--timeout', '180'], ['-l', '/large/large7.lay', '-c', '--timeout', '180'], ['-l', '/large/large8.lay', '-c', '--timeout', '180'], ['-l', '/large/large9.lay', '-c', '--timeout', '180'], ['-l', '/large/large10.lay', '-c', '--timeout', '180'], ['-l', '/large/large11.lay', '-c', '--timeout', '180'], ['-l', '/large/large12.lay', '-c', '--timeout', '180'], ['-l', '/large/large13.lay', '-c', '--timeout', '180'], ['-l', '/large/large14.lay', '-c', '--timeout', '180'], ['-l', '/large/large15.lay', '-c', '--timeout', '180'], ['-l', '/large/large16.lay', '-c', '--timeout', '180'], ['-l', '/large/large17.lay', '-c', '--timeout', '180'], ['-l', '/large/large18.lay', '-c', '--timeout', '180'], ['-l', '/large/large19.lay', '-c', '--timeout', '180'], ['-l', '/large/large20.lay', '-c', '--timeout', '180'], ['-l', '/large/large21.lay', '-c', '--timeout', '180'], ['-l', '/large/large22.lay', '-c', '--timeout', '180'], ['-l', '/large/large23.lay', '-c', '--timeout', '180'], ['-l', '/large/large24.lay', '-c', '--timeout', '180'], ['-l', '/large/large25.lay', '-c', '--timeout', '180'], ['-l', '/large/large26.lay', '-c', '--timeout', '180'], ['-l', '/large/large27.lay', '-c', '--timeout', '180'], ['-l', '/large/large28.lay', '-c', '--timeout', '180']]
Scores:  [-444.0, 712.0, 7.0, 768.0, 290.0, 467.0, -542.0, 926.0, -17.0, 880.0, 497.0, 265.0, 643.0, 296.0, 563.0, 874.0, 439.0, 313.0, -184.0, 718.0, -71.0, 1034.0, -305.0, -82.0, 898.0, 882.0, -386.0, 487.0] [-13.0, 1046.0, 289.0, 552.0, 547.0, 459.0, 316.0, 1525.0, 581.0, 2159.0, 709.0, 829.0, 773.0, 1291.0, 1807.0, 978.0, 1041.0, 2277.0, 1793.0, 867.0, 1973.0, 41.0, 707.0, 1320.0, 1573.0, 870.0, 379.0, 1119.0] [-36.0, 180.0, 108.0, -749.0, 131.0, 378.0, -460.0, 405.0, 99.0, 135.0, 207.0, 233.0, 108.0, 904.0, 305.0, -1510.0, 79.0, 81.0, -487.0, 271.0, 72.0, 126.0, 308.0, 295.0, 125.0, 162.0, 579.0, 36.0] [-109.0, -394.0, 36.0, -775.0, 137.0, 207.0, 1256.0, 117.0, 63.0, 27.0, 9.0, 54.0, 63.0, 534.0, 153.0, -736.0, 594.0, 36.0, -531.0, 291.0, 18.0, 117.0, 138.0, -20.0, 131.0, 9.0, 650.0, 9.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/large/large29.lay', '-c', '--timeout', '180']
Pacman died! Score: 782
Average Score: 782.0
Scores:        782.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/large/large29.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 1378.0
Scores:        1378.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/large/large29.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 33.0
Scores:        33.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/large/large29.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 112.0
Scores:        112.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', '/large/large1.lay', '-c', '--timeout', '180'], ['-l', '/large/large2.lay', '-c', '--timeout', '180'], ['-l', '/large/large3.lay', '-c', '--timeout', '180'], ['-l', '/large/large4.lay', '-c', '--timeout', '180'], ['-l', '/large/large5.lay', '-c', '--timeout', '180'], ['-l', '/large/large6.lay', '-c', '--timeout', '180'], ['-l', '/large/large7.lay', '-c', '--timeout', '180'], ['-l', '/large/large8.lay', '-c', '--timeout', '180'], ['-l', '/large/large9.lay', '-c', '--timeout', '180'], ['-l', '/large/large10.lay', '-c', '--timeout', '180'], ['-l', '/large/large11.lay', '-c', '--timeout', '180'], ['-l', '/large/large12.lay', '-c', '--timeout', '180'], ['-l', '/large/large13.lay', '-c', '--timeout', '180'], ['-l', '/large/large14.lay', '-c', '--timeout', '180'], ['-l', '/large/large15.lay', '-c', '--timeout', '180'], ['-l', '/large/large16.lay', '-c', '--timeout', '180'], ['-l', '/large/large17.lay', '-c', '--timeout', '180'], ['-l', '/large/large18.lay', '-c', '--timeout', '180'], ['-l', '/large/large19.lay', '-c', '--timeout', '180'], ['-l', '/large/large20.lay', '-c', '--timeout', '180'], ['-l', '/large/large21.lay', '-c', '--timeout', '180'], ['-l', '/large/large22.lay', '-c', '--timeout', '180'], ['-l', '/large/large23.lay', '-c', '--timeout', '180'], ['-l', '/large/large24.lay', '-c', '--timeout', '180'], ['-l', '/large/large25.lay', '-c', '--timeout', '180'], ['-l', '/large/large26.lay', '-c', '--timeout', '180'], ['-l', '/large/large27.lay', '-c', '--timeout', '180'], ['-l', '/large/large28.lay', '-c', '--timeout', '180'], ['-l', '/large/large29.lay', '-c', '--timeout', '180']]
Scores:  [-444.0, 712.0, 7.0, 768.0, 290.0, 467.0, -542.0, 926.0, -17.0, 880.0, 497.0, 265.0, 643.0, 296.0, 563.0, 874.0, 439.0, 313.0, -184.0, 718.0, -71.0, 1034.0, -305.0, -82.0, 898.0, 882.0, -386.0, 487.0, 782.0] [-13.0, 1046.0, 289.0, 552.0, 547.0, 459.0, 316.0, 1525.0, 581.0, 2159.0, 709.0, 829.0, 773.0, 1291.0, 1807.0, 978.0, 1041.0, 2277.0, 1793.0, 867.0, 1973.0, 41.0, 707.0, 1320.0, 1573.0, 870.0, 379.0, 1119.0, 1378.0] [-36.0, 180.0, 108.0, -749.0, 131.0, 378.0, -460.0, 405.0, 99.0, 135.0, 207.0, 233.0, 108.0, 904.0, 305.0, -1510.0, 79.0, 81.0, -487.0, 271.0, 72.0, 126.0, 308.0, 295.0, 125.0, 162.0, 579.0, 36.0, 33.0] [-109.0, -394.0, 36.0, -775.0, 137.0, 207.0, 1256.0, 117.0, 63.0, 27.0, 9.0, 54.0, 63.0, 534.0, 153.0, -736.0, 594.0, 36.0, -531.0, 291.0, 18.0, 117.0, 138.0, -20.0, 131.0, 9.0, 650.0, 9.0, 112.0]
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'MCTSAgent', '-l', '/large/large30.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 426.0
Scores:        426.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'BetterMCTSAgent', '-l', '/large/large30.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 1501.0
Scores:        1501.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'AlphaBetaAgent', '-l', '/large/large30.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 252.0
Scores:        252.0
Win Rate:      0/1 (0.00)
Record:        Loss
command:  ['python', 'pacman.py', '--frameTime', '0', '-q', '-p', 'ExpectimaxAgent', '-l', '/large/large30.lay', '-c', '--timeout', '180']
Pacman crashed
Average Score: 126.0
Scores:        126.0
Win Rate:      0/1 (0.00)
Record:        Loss
Environment:  [['-l', '/large/large1.lay', '-c', '--timeout', '180'], ['-l', '/large/large2.lay', '-c', '--timeout', '180'], ['-l', '/large/large3.lay', '-c', '--timeout', '180'], ['-l', '/large/large4.lay', '-c', '--timeout', '180'], ['-l', '/large/large5.lay', '-c', '--timeout', '180'], ['-l', '/large/large6.lay', '-c', '--timeout', '180'], ['-l', '/large/large7.lay', '-c', '--timeout', '180'], ['-l', '/large/large8.lay', '-c', '--timeout', '180'], ['-l', '/large/large9.lay', '-c', '--timeout', '180'], ['-l', '/large/large10.lay', '-c', '--timeout', '180'], ['-l', '/large/large11.lay', '-c', '--timeout', '180'], ['-l', '/large/large12.lay', '-c', '--timeout', '180'], ['-l', '/large/large13.lay', '-c', '--timeout', '180'], ['-l', '/large/large14.lay', '-c', '--timeout', '180'], ['-l', '/large/large15.lay', '-c', '--timeout', '180'], ['-l', '/large/large16.lay', '-c', '--timeout', '180'], ['-l', '/large/large17.lay', '-c', '--timeout', '180'], ['-l', '/large/large18.lay', '-c', '--timeout', '180'], ['-l', '/large/large19.lay', '-c', '--timeout', '180'], ['-l', '/large/large20.lay', '-c', '--timeout', '180'], ['-l', '/large/large21.lay', '-c', '--timeout', '180'], ['-l', '/large/large22.lay', '-c', '--timeout', '180'], ['-l', '/large/large23.lay', '-c', '--timeout', '180'], ['-l', '/large/large24.lay', '-c', '--timeout', '180'], ['-l', '/large/large25.lay', '-c', '--timeout', '180'], ['-l', '/large/large26.lay', '-c', '--timeout', '180'], ['-l', '/large/large27.lay', '-c', '--timeout', '180'], ['-l', '/large/large28.lay', '-c', '--timeout', '180'], ['-l', '/large/large29.lay', '-c', '--timeout', '180'], ['-l', '/large/large30.lay', '-c', '--timeout', '180']]
Scores:  [-444.0, 712.0, 7.0, 768.0, 290.0, 467.0, -542.0, 926.0, -17.0, 880.0, 497.0, 265.0, 643.0, 296.0, 563.0, 874.0, 439.0, 313.0, -184.0, 718.0, -71.0, 1034.0, -305.0, -82.0, 898.0, 882.0, -386.0, 487.0, 782.0, 426.0] [-13.0, 1046.0, 289.0, 552.0, 547.0, 459.0, 316.0, 1525.0, 581.0, 2159.0, 709.0, 829.0, 773.0, 1291.0, 1807.0, 978.0, 1041.0, 2277.0, 1793.0, 867.0, 1973.0, 41.0, 707.0, 1320.0, 1573.0, 870.0, 379.0, 1119.0, 1378.0, 1501.0] [-36.0, 180.0, 108.0, -749.0, 131.0, 378.0, -460.0, 405.0, 99.0, 135.0, 207.0, 233.0, 108.0, 904.0, 305.0, -1510.0, 79.0, 81.0, -487.0, 271.0, 72.0, 126.0, 308.0, 295.0, 125.0, 162.0, 579.0, 36.0, 33.0, 252.0] [-109.0, -394.0, 36.0, -775.0, 137.0, 207.0, 1256.0, 117.0, 63.0, 27.0, 9.0, 54.0, 63.0, 534.0, 153.0, -736.0, 594.0, 36.0, -531.0, 291.0, 18.0, 117.0, 138.0, -20.0, 131.0, 9.0, 650.0, 9.0, 112.0, 126.0]
"""


# Split the string into individual episodes based on the 'command' string
outputs = output.strip().split("command:")

# Remove empty strings and leading/trailing whitespaces from the episodes
outputs = [episode.strip() for episode in outputs if episode.strip()]

# Initialize counters
win_countSmall = {"MCTSAgent": 0, "BetterMCTSAgent": 0, "AlphaBetaAgent": 0, "ExpectimaxAgent": 0}
loss_countSmall = {"MCTSAgent": 0, "BetterMCTSAgent": 0, "AlphaBetaAgent": 0, "ExpectimaxAgent": 0}

win_countMedium = {"MCTSAgent": 0, "BetterMCTSAgent": 0, "AlphaBetaAgent": 0, "ExpectimaxAgent": 0}
loss_countMedium = {"MCTSAgent": 0, "BetterMCTSAgent": 0, "AlphaBetaAgent": 0, "ExpectimaxAgent": 0}

# Parse the outputs and count wins and losses for each agent
for output in outputs:
    # Split the command string into individual elements
    elements = output.split('\n')
    print(elements[0].split()[6][1:-2])

    print(elements[0].split()[8])
    print(elements[5])

    agentName = elements[0].split()[6][1:-2]

    layout = elements[0].split()[8]
    if 'Classic' in layout or 'small' in layout:
        layout = 'small'
    elif 'medium' in layout:
        layout = 'medium'
    elif 'large' in layout:
        layout = None

    winRecord = elements[5]
    if 'Win' in winRecord:
        winRecord = 1
    else:
        winRecord = 0

    print(agentName, layout, winRecord)

    if layout is not None:
        if layout is 'small':
            if winRecord > 0:
                win_countSmall[agentName] += 1
            else:
                loss_countSmall[agentName] += 1

        if layout is 'medium':
            if winRecord > 0:
                win_countMedium[agentName] += 1
            else:
                loss_countMedium[agentName] += 1

# Calculate win percentages small
win_percentages = {}
for agent, wins in win_countSmall.items():
    total_episodes = wins + loss_countSmall[agent]
    win_percentages[agent] = wins / total_episodes if total_episodes != 0 else 0

# Print win percentages
for agent, win_percentage in win_percentages.items():
    print(f"Win percentage for {agent} Small Layouts: {100 * win_percentage:.2f}")

# Calculate win percentages medium
win_percentages = {}
for agent, wins in win_countMedium.items():
    total_episodes = wins + loss_countMedium[agent]
    win_percentages[agent] = wins / total_episodes if total_episodes != 0 else 0

# Print win percentages
for agent, win_percentage in win_percentages.items():
    print(f"Win percentage for {agent} Medium Layouts: {100 * win_percentage:.2f}")
