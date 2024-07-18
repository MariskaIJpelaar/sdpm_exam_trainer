from random import randrange

from sdpm_exam_trainer.core.question import Question
from sdpm_exam_trainer.utils.printer import *

class QuestionNPV(Question):
	def __init__(self):
		super(QuestionNPV, self).__init__()
		self.weight = 0.5
		self.nr_years = 3
		self.multiple = 5000
		self.range = 10
		self.interest = 0.1
		self.generate_table()

	def generate_table(self):
		self.table = {}
		for x in range(self.nr_years):
			fv = randrange(self.range) * self.multiple
			pv = int((fv / ((1+self.interest)**x))+0.5)
			self.table[x] = [fv, pv]

	# return the number of points received for this question [0, 1]
	# the number of points is determined interactively
	def grade(self):
		printc(Color.CAN, 'Calculate the present value (pv) for each year for an interest rate of {}%, given the following future values (fvs)'.format(self.interest*100))
		printc(Color.CAN, '{:<4} {:<7}'.format('Year', 'FV'))
		for year, values in self.table.items():
			printc(Color.CAN, '{:<4} {:<7}'.format(year, values[0]))

		correct = 0
		for year, values in self.table.items():
			printc(Color.BLU, 'What is the PV for year {}?'.format(year))
			correct += self.check(str(values[1]))
		return correct / len(self.table) 