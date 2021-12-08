from random import randrange, random

from grader.core.defs import QuestionDefs
from grader.utils.printer import *

class QuestionShareGrowthDefs(QuestionDefs):
	def __init__(self):
		super(QuestionShareGrowthDefs, self).__init__()
		self.weight = 0.2

	def generate_pairs(self):
		return [
			('Stars', 'high market growth rate, high market share'),
			('Question Marks', 'high market growth rate, low market share'),
			('Cash Cow', 'low market growth rate, high market share'),
			('Dogs', 'low market growth rate, low market share')
		]