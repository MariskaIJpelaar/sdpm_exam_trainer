from random import randrange, random

from grader.core.question import Question
from grader.utils.printer import *

class QuestionDefs(Question):
	def __init__(self):
		super(QuestionDefs, self).__init__()
		self.pairs = self.generate_pairs()
		self.match_shuffled()

	# sets self.pairs to a list of item-definition pairs
	def generate_pairs(self):
		raise NotImplementedError

	def match_shuffled(self):
		self.matched = [ x for x in sorted(list(range(len(self.pairs))),key=lambda _: random())]

	# return the number of points received for this question [0, 1]
	# the number of points is determined interactively
	def grade(self):
		printc(Color.CAN, 'You are given the following definitions:')
		for i, x in enumerate(self.matched):
			printc(Color.CAN, '\t{}) {}'.format(i, self.pairs[x][1]))

		points = 0
		for i, pair in enumerate(self.pairs):
			printc(Color.BLU, 'Give the number which matches the definition of ', pair[0])
			points += self.check(str(self.matched.index(i)))

		return points / len(self.pairs)