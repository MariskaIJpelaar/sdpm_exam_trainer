from random import randrange

from grader.core.question import Question
from grader.utils.printer import *

class QuestionEVA(Question):
	def __init__(self):
		super(QuestionEVA, self).__init__()
		self.weight = 0.5
		self.nr_months = 5
		self.multiple = 10
		self.range = 20
		self.unitprice = randrange(5)+1
		self.generate_table()

	def generate_table(self):
		# Month, Planned Cost, Actual Cost, Meters / Earned Value
		self.table = {}
		planned = 0 
		actual = 0 
		meters = 0
		for x in range(self.nr_months):
			planned += (randrange(self.range)*self.multiple)
			actual += (randrange(self.range)*self.multiple)
			meters += (randrange(self.range)*self.multiple)
			self.table[x] = [planned, actual, meters]

	# return the number of points received for this question [0, 1]
	# the number of points is determined interactively
	def grade(self):
		printc(Color.CAN, 'You are given the following information:')
		printc(Color.CAN, '{:<5} {:<12} {:<11} {:<6}'.format('Month', 'Planned Cost', 'Actual Cost', 'Meters'))
		for month, values in self.table.items():
			printc(Color.CAN, '{:<5} {:<12} {:<11} {:<6}'.format(month, values[0], values[1], values[2]))
		printc(Color.CAN, 'Each meter costs {} euro(s) and earns back twice as much'.format(self.unitprice))

		points = 0
		questions = 0
		month = randrange(self.nr_months)

		printc(Color.BLU, 'What is the Planned Value (PV) for month {}?'.format(month))
		pv = self.table[month][0]
		points += self.check(str(pv))
		questions += 1

		printc(Color.BLU, 'What is the Actual Cost (AC) for month {}?'.format(month))
		ac = self.table[month][1]
		points += self.check(str(ac))
		questions += 1

		printc(Color.BLU, 'What is the Earned Value (EV) for month {}?'.format(month))
		ev = self.table[month][2]*self.unitprice*2
		points += self.check(str(ev))
		questions += 1

		printc(Color.BLU, 'What is the Scheduled Variance (SV) for month {}?'.format(month))
		points += self.check(str(ev - pv))
		questions += 1

		printc(Color.BLU, 'What is the Cost Variance (CV) for month {}?'.format(month))
		points += self.check(str(ev - ac))
		questions += 1

		printc(Color.BLU, 'What is the Scheduled Performance Indicator (SPI) for month {}?'.format(month))
		points += self.check(str(int((ev / pv)+0.5)))
		questions += 1

		printc(Color.BLU, 'What is the Cost Performance Indicator (CPI) for month {}?'.format(month))
		points += self.check(str(int((ev / ac)+0.5)))
		questions += 1

		return points / questions