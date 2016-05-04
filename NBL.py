# Naive Bayes Learner class

class NBL:
    # priorProbabilities = {}  # probability of class being 1 given an attribute being 1
    # classProbabilities = {}
    attributes = []
    attrInfo = {} #attr probability-relevant info
    enumKeys = ['negative', 'positive']
    trainingdata = []
    digitsToRoundTo = 3

    def __init__(self, trainingdata, attributes):
        self.trainingdata = trainingdata
        self.attributes = attributes
        self.calculateProbabilities(trainingdata)

    # calculate probabilities based on training data, store in attrInfo
    def calculateProbabilities(self, trainingdata):
        attrInfo = {}
        for attribute in self.attributes:
            attrInfo[attribute] = {
                "positive": { # meaning, when this attribute is positive
                    "name": attribute,
                    "total": 0,
                    "positiveClass": 0, # meaning, the number of positive classifications associated w/ this attr value
                    "negativeClass": 0  # meaning, the number of negative classifications associated w/ this attr value
                },
                "negative": {
                    "name": attribute,
                    "total": 0,
                    "positiveClass": 0,
                    "negativeClass": 0
                }
            }
        for data in trainingdata:
            for attr in data.keys():
                if data[attr] is 1:
                    attrInfo[attr]['positive']['total'] += 1
                    if data['class'] is 1:
                        attrInfo[attr]['positive']['positiveClass'] += 1
                    else:
                        attrInfo[attr]['positive']['negativeClass'] += 1
                else:
                    attrInfo[attr]['negative']['total'] += 1
                    if data['class'] is 1:
                        attrInfo[attr]['negative']['positiveClass'] += 1
                    else:
                        attrInfo[attr]['negative']['negativeClass'] += 1
        self.attrInfo = attrInfo

    # print probabilities after training
    def printProbabilities(self):
        print("PRINTING PARAMETERS")
        for classification in range(0, 2):
            printStr = ""
            printStr += self.printProbability(self.attrInfo['class'][self.enumKeys[classification]], classification, classification)
            for key, value in self.attrInfo.items():
                if key != 'class':
                    printStr += self.printProbability(value[self.enumKeys[0]], classification, 0)
                    printStr += self.printProbability(value[self.enumKeys[1]], classification, 1)
            print(printStr)

    # print an individual probability
    def printProbability(self, attrObj, classification, attrValue):
        stringTemplate = "P({0}={1}{2})="
        stringifiedClassification = str(classification)
        if attrObj['name'] == 'class':
            return stringTemplate.format(attrObj['name'], stringifiedClassification, "") + str(self.priorProbability(classification))
        else:
            return stringTemplate.format(attrObj['name'], attrValue, "|class=" + stringifiedClassification)+ str(self.attrProbability(attrObj, classification))

    # return attr probability for a given class
    def attrProbability(self, attrObj, classValue):
        enumClassKeys = ["negativeClass", "positiveClass"]
        numerator = attrObj[enumClassKeys[classValue]]
        total = attrObj['total']
        if total == 0:
            returnVal = 0
        else:
            returnVal = round((numerator / total), self.digitsToRoundTo)
        return returnVal

    # return prior probability value
    def priorProbability(self, classValue):
        numerator = self.attrInfo['class'][self.enumKeys[classValue]]['total']
        total = len(self.trainingdata)
        if total == 0:
            returnVal = 0
        else:
            returnVal = round((numerator / total), self.digitsToRoundTo)
        return returnVal

    # classify a list of data
    def classifyData(self, data, nameOfData):
        print("CLASSIFYING " + nameOfData)
        numCorrect = 0
        totalItems = len(data)
        for item in data:
            numCorrect += self.classifyInstance(item)
        accuracy = round(numCorrect / totalItems, self.digitsToRoundTo) * 100
        print("Accuracy on {} ({} instances): {}%".format(nameOfData, str(totalItems), str(accuracy)))

    # use learned naive bayes to classify an instance
    def classifyInstance(self, instance):
        guess = 2
        prevGuessProbability = 0
        for classValue in range(0, 2):
            priorProb = self.priorProbability(classValue)
            runningProb = priorProb
            for attrKey, attrValue in self.attrInfo.items():
                if attrKey != 'class':
                    instanceVal = instance[attrKey]
                    conditionalProb = self.attrProbability(attrValue[self.enumKeys[instanceVal]], classValue)
                    runningProb = runningProb * conditionalProb
            if runningProb > prevGuessProbability:
                guess = classValue
            prevGuessProbability = runningProb
        if str(guess) == str(instance['class']):
            return 1
        else:
            return 0

