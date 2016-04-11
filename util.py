# Util file for Naive Bayes Project

# reads file
# returns (attributes, dataArray)
def readFile(filepath):
    attributes = []
    data = []
    f = open(filepath, 'r')
    fileLines = list(f)
    attributes = fileLines[0].split()
    for line in fileLines[1:]:
        dictItem = dict(zip(attributes, line.split()))
        data.append(dictItem)
    return attributes, data