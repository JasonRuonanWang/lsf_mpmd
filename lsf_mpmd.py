import sys
import os

ranksPerNode = 40
cpusPerRank = 4

params={}
params["cpu_index_using"] = "physical"
params["overlapping_rs"] = "warn"
params["skip_missing_cpu"] = "warn"
params["skip_missing_gpu"] = "allow"
params["skip_missing_mem"] = "allow"
params["oversubscribe_cpu"] = "error"
params["oversubscribe_gpu"] = "allow"
params["oversubscribe_mem"] = "allow"
params["launch_distribution"] = "packed"

rankCurrent = 0
appCurrent = 0
cpuCurrent = 0

apps = []
ranks = []

for arg in range(1, len(sys.argv), 2):
    apps.append(os.getcwd() + "/" + sys.argv[arg])
    ranks.append(int(sys.argv[arg+1]))

ranksTotal = sum(ranks)

file1 = open("job.erf","w")

s = 0
for app in apps:
    file1.write("app {0}: {1}".format(s, app) + "\n")
    s = s + 1

for key, value in params.items():
    file1.write(key + ": " + value + "\n")

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

