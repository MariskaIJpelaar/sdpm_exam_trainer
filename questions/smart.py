from random import randrange, random

from grader.core.acronyms import QuestionAcronym
from grader.utils.printer import *

class QuestionSMART(QuestionAcronym):
	def __init__(self):
		super(QuestionSMART, self).__init__()
		self.weight = 0.5

	# returns a list of letter-description pairs of the acronym
	def define_acronym(self):
		return [
			('S', 'specific'), 
			('M', 'measurable'), 
			('A', 'agreed upon'),
			('R', 'realistic'),
			('T', 'time based')
		]