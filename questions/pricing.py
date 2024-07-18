from random import randrange, random

from sdpm_exam_trainer.core.defs import QuestionDefs
from sdpm_exam_trainer.utils.printer import *

class QuestionPricingDefs(QuestionDefs):
	def __init__(self):
		super(QuestionPricingDefs, self).__init__()
		self.weight = 0.3

	def generate_pairs(self):
		return [
			('Premium price strategy', 'high price, high quality'), 
			('Price differentiation, strategy', 'same product, different prices'),
			('Penetration strategy', 'low price for rapid market share grow'),
			('Skimming price strategy', 'high price as compensation for high investment'),
			('Life-cycle-dependent pricing strategy', 'situation-specific'), 
			('Non-linear pricing strategy', 'has a usage-based component and a usage-independent component')
		]