import util
import sys

args = sys.argv
#arg[1] is training data
#arg[2] is test data
attributes, trainingData = util.readFile(args[1])
testAttributes, testData = util.readFile(args[2])