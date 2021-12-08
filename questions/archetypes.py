from random import randrange, random

from grader.core.defs import QuestionDefs
from grader.utils.printer import *

class QuestionArchetypesDefs(QuestionDefs):
	def __init__(self):
		super(QuestionArchetypesDefs, self).__init__()
		self.weight = 0.2

	def generate_pairs(self):
		return [
			('Creator', 'designs and/or produces a product sold to customers'),
			('Distributor', 'buys a product and provides the same product to customers'),
			('Lessor', 'provides the temporary right to use, but not own, a product or service to customers'),
			('Broker', 'facilitates the matching of potential buyers and sellers')
		]