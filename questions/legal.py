from random import randrange, random

from grader.core.defs import QuestionDefs
from grader.utils.printer import *

class QuestionLegalDefs(QuestionDefs):
	def __init__(self):
		super(QuestionLegalDefs, self).__init__()
		self.weight = 0.2

	def generate_pairs(self):
		return [
			('Trademark', 'protection for the names of brands'),
			('Copyright', 'protection against copying of software code and product material'),
			('Patent', 'protection of a specific technical concept or idea'),
			('Escrow', 'a service where a 3rd party holds source code, data and documentation, until a mutually-agreed-upon event occurs')
		]