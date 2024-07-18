from random import randrange
from math import sqrt

from sdpm_exam_trainer.core.question import Question
from sdpm_exam_trainer.utils.printer import *

class QuestionPERT(Question):
	def __init__(self):
		super(QuestionPERT, self).__init__()
		self.weight = 1
		self.range = 50
		self.generate_table()

	def generate_table(self):
		self.table = {}
		activities = ['A', 'B']
		for activity in activities:
			optimistic = randrange(self.range)
			normal = optimistic + randrange(self.range)
			pessimistic = normal + randrange(self.range)
			self.table[activity] = [optimistic, normal, pessimistic]

	# return the number of points received for this question [0, 1]
	# the number of points is determined interactively
	def grade(self):
		printc(Color.CAN, 'You are given the following information:')
		printc(Color.CAN, '{:<20} {:<10} {:<6} {:<11}'.format('Critical Activities', 'Optimistic', 'Normal', 'Pessimistic'))
		for activity, values in self.table.items():
			printc(Color.CAN, '{:<20} {:<10} {:<6} {:<11}'.format(activity, values[0], values[1], values[2]))

		points = 0
		questions = 0
		total = 0.0
		total_var = 0.0
		for activity, values in self.table.items():
			printc(Color.BLU, 'What is the expected duration of Activity {}?'.format(activity))
			correct = int(((values[0] + 4 * values[1] + values[2]) / 6)+0.5)
			points += self.check(str(correct))
			total += correct
			questions += 1

			printc(Color.BLU, 'What is the standard deviation of Activity {}?'.format(activity))
			stdev = int(((values[2] - values[0])/6) + 0.5)
			points += self.check(str(stdev))
			questions += 1

			printc(Color.BLU, 'What is the variance of Activity {}?'.format(activity))
			var = int((stdev ** 2) + 0.5)
			total_var += var
			points += self.check(str(var))
			questions += 1

		printc(Color.BLU, 'What is the expected duration of the total critical path?')
		points += self.check(str(int(total)))
		questions += 1

		printc(Color.BLU, 'What is the variance of the total critical path?')
		points += self.check(str(int(total_var)))
		questions += 1

		printc(Color.BLU, 'What is the standard deviation of the total critical path?')
		points += self.check(str(int(sqrt(total_var)+0.5)))
		questions += 1

		printn('This question did not include working with the Z-table!')
		return points / questions