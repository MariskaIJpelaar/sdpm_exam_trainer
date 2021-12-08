from random import randrange, random

from grader.core.defs import QuestionDefs
from grader.utils.printer import *

class QuestionWBSDefs(QuestionDefs):
	def __init__(self):
		super(QuestionWBSDefs, self).__init__()
		self.weight = 0.2

	def generate_pairs(self):
		return [
			('Planning packages', 'a component about which we still have insufficient information to split it up further'), 
			('Control accounts', 'an in-between level over which we let the sub-project managers (or suppliers) report'),
			('Work packages', 'the lowest level at which it is possible to identify the activities to be carried out by the team and to make realistic estimates')
		]