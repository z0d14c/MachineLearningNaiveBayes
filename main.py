# thomas grice tag130230
import util
import sys
import NBL

args = sys.argv
#arg[1] is training data
#arg[2] is test data
attributes, trainingData = util.readFile(args[1])

# train the NBL
naivebayeslearner = NBL.NBL(trainingData, attributes)
naivebayeslearner.printProbabilities()

# test on training data
naivebayeslearner.classifyData(trainingData, "training set")

testAttributes, testData = util.readFile(args[2])
naivebayeslearner.classifyData(testData, "test set")
