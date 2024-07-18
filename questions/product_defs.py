from random import randrange, random

from sdpm_exam_trainer.core.defs import QuestionDefs
from sdpm_exam_trainer.utils.printer import *

class QuestionProductDefs(QuestionDefs):
	def __init__(self):
		super(QuestionProductDefs, self).__init__()
		self.weight = 0.2

	def generate_pairs(self):
		return [
			('Product Platform', 'The technical foundation on which several software products are based'),
			('Product Family', 'a group of software products that are marketed as belonging together under a common family name (e.g. Microsoft Office)'),
			('Product Line', 'a set of products based on a common platform with defined (static or dynamic) variability tailored to different markets and users'),
			('Solution', 'A product that is a combination of other products, human services, and possibly some glue code and customization')
		]