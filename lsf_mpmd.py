ranks = [200, 20]
ranksPerNode = 40
cpusPerRank = 4

ranksTotal = sum(ranks)
rankCurrent = 0
appCurrent = 0
cpuCurrent = 0

file1 = open("job.erf","w")


for app in ranks:
    for rank in range(app):
        if rankCurrent % ranksPerNode == 0:
            cpuCurrent = 0
        host = int(rankCurrent / ranksPerNode)
        line = "rank: {0}: {{ host: {1}; cpu: {{{2}-{3}}} }} : app {4}".format(rankCurrent, host, cpuCurrent, cpuCurrent + 3, appCurrent)
        file1.write(line + "\n")
        cpuCurrent = cpuCurrent + cpusPerRank
        rankCurrent = rankCurrent + 1
    appCurrent = appCurrent + 1


