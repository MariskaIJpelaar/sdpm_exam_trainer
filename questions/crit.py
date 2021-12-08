from grader.core.question import Question
from grader.utils.printer import *

class QuestionCriticalPath(Question):
	def __init__(self):
		super(QuestionCriticalPath, self).__init__()
		self.weight = 1.0
		# Activity, Duration, Start
		self.table = {
			'A': [10, ''],
			'B': [15, 'After A'],
			'C': [30, 'After B and D'],
			'D': [20, 'After A'],
			'E': [20, 'After D'],
			'F': [5, 'After E'],
			'G': [40, 'After A'],
			'H': [5, 'After C, F and G']
		}

	# return the number of points received for this question [0, 1]
	# the number of points is determined interactively
	def grade(self):
		printn('This Question does not include drawing resource utilization')
		printc(Color.CAN, 'Determine the Critical Path for the following table:')
		printc(Color.CAN, '{:<8} {:<8} {:<5}'.format('Activity', 'Duration', 'Start'))
		for activity, values in self.table.items():
			printc(Color.CAN, '{:<8} {:<8} {:<5}'.format(activity, values[0], values[1]))

		printc(Color.BLU, 'What is the critical path? (format: XYZ, with X, Y, Z activity identifiers)')
		return self.check('ADCH')