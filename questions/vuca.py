from random import randrange, random

from grader.core.acronyms import QuestionAcronym
from grader.utils.printer import *

class QuestionVUCA(QuestionAcronym):
	def __init__(self):
		super(QuestionVUCA, self).__init__()
		self.weight = 0.5

	# returns a list of letter-description pairs of the acronym
	def define_acronym(self):
		return [
			('V', 'volatility'),
			('U', 'uncertainty'), 
			('C', 'complexity'), 
			('A', 'ambiguity')
		]