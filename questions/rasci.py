from random import randrange, random

from grader.core.acronyms import QuestionAcronym
from grader.utils.printer import *

class QuestionRASCI(QuestionAcronym):
	def __init__(self):
		super(QuestionRASCI, self).__init__()
		self.weight = 0.5

	# returns a list of letter-description pairs of the acronym
	def define_acronym(self):
		return [
			('R', 'responsible'), 
			('A', 'accountable'), 
			('S', 'support'), 
			('C', 'consult'),
			('I', 'inform')
		]