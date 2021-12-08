from random import randrange

from grader.core.question import Question
from grader.utils.printer import *

class QuestionOpportunityCost(Question):
	def __init__(self):
		super(QuestionOpportunityCost, self).__init__()
		self.weight = 0.2
		self.multiple = 5000
		self.range = 20
		self.projectA = (randrange(self.range)+1) * self.multiple
		self.projectB = (randrange(self.range)+1) * self.multiple

	# return the number of points received for this question [0, 1]
	# the number of points is determined interactively
	def grade(self):
		printc(Color.CAN, 'You have two projects to choose from: ')
		printc(Color.CAN, '\t- Project A with an NPV of ${} OR'.format(self.projectA))
		printc(Color.CAN, '\t- Project B with an NPV of ${}'.format(self.projectB))
		chooser = randrange(2)
		chosen = 'A' if chooser == 0 else 'B'
		correct = self.projectB if chooser == 0 else self.projectA
		printc(Color.BLU, 'What is the opportunity cost of selecting project {}?'.format(chosen))
		return self.check(str(correct))