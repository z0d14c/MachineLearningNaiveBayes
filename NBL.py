# Naive Bayes Learner class

class NBL:
    priorProbabilities = {} # probability of class being 1 given an attribute being 1
    classProbabilities = {}
    attributes = []

    def __init__(self, trainingdata, attributes):
        self.calculateProbabilities(trainingdata)

    # calculate probabilities based on training data
    def calculateProbabilities(self, trainingdata):
        attrInfo = {}
        for attribute in self.attributes:
            attrInfo[attribute] = {
                "totalPositive":0,
                "totalNegative":0,
                "class1WhenPositive":0,
                "class1WhenNegative":0
            }

