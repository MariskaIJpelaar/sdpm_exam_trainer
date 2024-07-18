from random import randrange, random

from sdpm_exam_trainer.core.defs import QuestionDefs
from sdpm_exam_trainer.utils.printer import *

class QuestionScenariosDefs(QuestionDefs):
	def __init__(self):
		super(QuestionScenariosDefs, self).__init__()
		self.weight = 0.2

	def generate_pairs(self):
		return [
			('Powerboat', 'new product, vendor-controlled, main focus: exciters, delighters'),
			('Speedboat', 'existing product, vendor-controlled, main focus: satisfiers, wants'),
			('Icebreakers', 'new product, customer-controlled, pitfall: too much focus on dissatisfiers/ musts'),
			('Cruise ship', 'existing product, customer-controlled, pitfall: indifferent attributes')
		]