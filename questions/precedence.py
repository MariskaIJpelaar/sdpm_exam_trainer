from random import randrange, random

from sdpm_exam_trainer.core.defs import QuestionDefs
from sdpm_exam_trainer.utils.printer import *

class QuestionPrecedenceDefs(QuestionDefs):
	def __init__(self):
		super(QuestionPrecedenceDefs, self).__init__()
		self.weight = 0.3

	def generate_pairs(self):
		return [
			('Critical path', 'A path through the network with zero floats'), 
			('Total float', 'Time you can start later without delaying the project'),
			('Free float', 'Time you can start later without delaying another activity'),
			('Lag', 'There is a \'gap\' between two activities'),
			('Lead', 'Two activities are dependent but can overlap'),
			('Finish-to-Start', 'First activity must finish before second activity can start'),
			('Start-to-Start', 'First activity must start before second activity can start'),
			('Finish-to-Finish', 'First activity must finish before second activity can finish'),
			('Start-to-Finish', 'First activity must start before second activity can finish')
		]