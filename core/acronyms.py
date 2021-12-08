from random import randrange, random

from grader.core.question import Question
from grader.utils.printer import *

class QuestionAcronym(Question):
	def __init__(self):
		super(QuestionAcronym, self).__init__()
		self.acronym_defs = self.define_acronym()
		self.generate_acronym()

	# returns a list of letter-description pairs of the acronym
	def define_acronym(self):
		raise NotImplementedError
	
	def generate_acronym(self):
		self.acronym = '.'.join([x for x, _ in self.acronym_defs])

	# return the number of points received for this question [0, 1]
	# the number of points is determined interactively
	def grade(self):
		points = 0
		for letter, description in self.acronym_defs:
			printc(Color.BLU, 'What does {} in {} stand for?'.format(letter, self.acronym))
			points += self.check(description) 

		return points / len(self.acronym_defs)