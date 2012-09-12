..\texf.py GAME_1_PF.log "\d+-\d+\d+ \d+:\d+:\d+ INFO  - .+:(\d+\.\d+) ms: .+:(.+)\s*$" > pf.csv
..\map.py pf.csv 1 > tex.csv