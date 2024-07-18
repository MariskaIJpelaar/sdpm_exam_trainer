from random import randrange, random

from sdpm_exam_trainer.core.defs import QuestionDefs
from sdpm_exam_trainer.utils.printer import *

class QuestionSchedulesDefs(QuestionDefs):
	def __init__(self):
		super(QuestionSchedulesDefs, self).__init__()
		self.weight = 0.2

	def generate_pairs(self):
		return [
			('Activity schedule', 'schedule indicating start and completion dates for each activity'), 
			('Resource schedule', 'schedule indicating dates when resources are needed + the lever of these resources'),
			('Cost schedule', 'schedule showing accumulative expenditure')
		]