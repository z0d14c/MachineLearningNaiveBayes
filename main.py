import util
import sys
import NBL

args = sys.argv
#arg[1] is training data
#arg[2] is test data
attributes, trainingData = util.readFile(args[1])

naivebayeslearner = NBL.NBL(trainingData, attributes)


testAttributes, testData = util.readFile(args[2])
